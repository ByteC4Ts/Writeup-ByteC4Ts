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
        offset, ch = bytes([offset]), bytes([ord(ch)])
        payload += b"\x01" + ch  # push(ch)
        payload += b"\x02\x07"  # pop(R7)
        payload += b"\x07" + offset + b"\x07"  # store(offset, R7)
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


payload = store("HELLO WORLD!") + output(12) + b"\x00"
print(payload)
print(send(payload))  # HELLO WORLD!Thanks for playing
