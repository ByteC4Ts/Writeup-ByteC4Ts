from challengeio import send

"""
Instructions:

\x00: 0 opt(s),             halt
\x01: 1 opt(s), data        push (imm)
\x02: 1 opt(s), Rx          pop  (Rx)
\x03: 1 opt(s), Rx          push (Rx)
\x04: 1 opt(s), Rx          or   (Rx)       => R0 |= Rx
\x05: 1 opt(s), Rx          xor  (Rx)       => R0 ^= Rx
\x06: 2 opt(s), Rx, addr    load (Rx, data) => Rx = mem[addr]
\x07: 2 opt(s), addr, Rx    store(addr, Rx) => mem[addr] = Rx

\x08: 0 opt(s),             syscall
                            R0         R1     R2     R3
                            0: read   (fd,    addr,  size)
                            1: write  (fd,    addr,  size)
                            2: open   (path,  flags)
                            3: close  (fd)
"""


def store(s):
    payload = b""
    for offset, ch in enumerate(s):
        offset = bytes([offset])
        # 'f','l','a','g' is forbidden
        if ch in "flag":
            ch_xor_0xff = bytes([ord(ch) ^ 0xFF])
            payload += b"\x01" + ch_xor_0xff  # push(ch ^ 0xFF)
            payload += b"\x02\x00"  # pop(R0)
            payload += b"\x01\xff"  # push(0xFF)
            payload += b"\x02\x07"  # pop(R7)
            payload += b"\x05\x07"  # R0 ^= R7
            payload += b"\x07" + offset + b"\x00"  # store(offset, R0)
        else:
            ch = bytes([ord(ch)])
            payload += b"\x01" + ch  # push(ch)
            payload += b"\x02\x07"  # pop(R7)
            payload += b"\x07" + offset + b"\x07"  # store(offset, R7)
    return payload


def open():
    payload = b"\x01\x02"  # push(2) -> R0, syscall_number = 2 (open)
    payload += b"\x01\x00"  # push(0) -> R1, path_addr = 0x00 (flag.txt)
    payload += b"\x01\x00"  # push(0) -> R2, flags = 0 (read-only)
    payload += b"\x02\x02\x02\x01\x02\x00"  # pop(R2), pop(R1), pop(R0)
    payload += b"\x08"  # syscall
    payload += b"\x03\x00\x02\x06"  # push(R0), pop(R6) -> R6 = fd
    payload += b"\x08"  # syscall
    return payload


def read(size):
    size = bytes([size])
    payload = b"\x01\x00"  # push(0) -> R0, syscall_number = 0 (read)
    payload += b"\x03\x06"  # push(R6) -> R1, fd = R6 (result of open syscall)
    payload += b"\x01\x00"  # push(0) -> R2, start_addr = 0x00
    payload += b"\x01" + size  # push(size) -> R3
    payload += b"\x02\x03\x02\x02\x02\x01\x02\x00"  # pop(R3), pop(R2), pop(R1), pop(R0)
    payload += b"\x08"  # syscall
    return payload


def output(size):
    size = bytes([size])
    payload = b"\x01\x01"  # push(1) -> R0, syscall_number = 1 (write)
    payload += b"\x01\x01"  # push(1) -> R1, fd = 1 (stdout)
    payload += b"\x01\x00"  # push(0) -> R2, start_addr = 0x00
    payload += b"\x01" + size  # push(size) -> R3
    payload += b"\x02\x03\x02\x02\x02\x01\x02\x00"  # pop(R3), pop(R2), pop(R1), pop(R0)
    payload += b"\x08"  # syscall
    return payload


size = 45
payload = store("flag.txt") + open() + read(size) + output(size) + b"\x00"
print(payload)
print(send(payload))  # idek{Th15_I$_thE_L@Z13$t_vM_i_h4vE_EvEr_5EEN}Thanks for playing

# idek{Th15_I$_thE_L@Z13$t_vM_i_h4vE_EvEr_5EEN}
