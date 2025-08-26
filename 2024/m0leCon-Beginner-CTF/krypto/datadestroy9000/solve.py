from pwn import process, context, xor

context.log_level = 'debug'

io = process(['python3', '2024/m0leconctf/datadestroy9000/chall.py'])

io.recvuntil(b'secret hehe\n')
enc_flag = bytes.fromhex(io.recvline().strip().decode())
enc_flag = [list(enc_flag[i : i + 32]) for i in range(0, len(enc_flag), 32)]


CS, BS = 128, 32


def diff(a, b):
    for i in range(len(a)):
        if (a[i] - b[i]) != 0:
            return i
    return -1



io.sendlineafter(b'> ', b'00')
enc_otp = bytes.fromhex(io.recvline().strip().decode())
enc_otp = [list(enc_otp[i : i + 32]) for i in range(0, len(enc_otp), 32)]


perms = []
for block in range(CS // BS):
    perm = []
    for i in range(BS):
        payload = (block * 32 * b'\x00') + (i * b'\x00') + b'\x01'
        io.sendlineafter(b'> ', payload.hex().encode())
        c_test = bytes.fromhex(io.recvline().strip().decode())[block * BS: (block + 1) * BS]
        perm.append(diff(enc_otp[block], c_test))
    perms.append(perm)


otp = []
for perm, oc in zip(perms, enc_otp):
    otp.append([oc[perm[i]] for i in range(BS)])

flag = []
for perm, ec in zip(perms, enc_flag):
    flag.append([ec[perm[i]] for i in range(BS)])


otp = bytes(sum(otp, []))
flag = bytes(sum(flag, []))

print(xor(otp, flag))