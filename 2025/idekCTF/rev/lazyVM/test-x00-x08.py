from challengeio import send

for i in range(10):
    print(f"Instruction {i}:")
    for opt in ["\x00\x00", "\x04\x00", "\x08\x00", "\x99\x00",
                "\x04\x06\x00", "\x04\x99\x00", "\x99\x06\x00", "\x99\x99\x00"]:
        payload = bytes([i]) + opt.encode("latin1")
        print(payload + b"\n", send(payload))
    print("========")

"""
Instruction 0:
b'\x00\x00\x00\n' Thanks for playing
b'\x00\x04\x00\n' Thanks for playing
b'\x00\x08\x00\n' Thanks for playing
b'\x00\x99\x00\n' Thanks for playing
b'\x00\x04\x06\x00\n' Thanks for playing
b'\x00\x04\x99\x00\n' Thanks for playing
b'\x00\x99\x06\x00\n' Thanks for playing
b'\x00\x99\x99\x00\n' Thanks for playing
========
Instruction 1:
b'\x01\x00\x00\n' Thanks for playing
b'\x01\x04\x00\n' Thanks for playing
b'\x01\x08\x00\n' Thanks for playing
b'\x01\x99\x00\n' Thanks for playing
b'\x01\x04\x06\x00\n' Thanks for playing
b'\x01\x04\x99\x00\n' Unknown instruction at ip=0x2
b'\x01\x99\x06\x00\n' Thanks for playing
b'\x01\x99\x99\x00\n' Unknown instruction at ip=0x2
========
Instruction 2:
b'\x02\x00\x00\n' Thanks for playing
b'\x02\x04\x00\n' Thanks for playing
b'\x02\x08\x00\n' reg index out of range
b'\x02\x99\x00\n' reg index out of range
b'\x02\x04\x06\x00\n' Thanks for playing
b'\x02\x04\x99\x00\n' Unknown instruction at ip=0x2
b'\x02\x99\x06\x00\n' reg index out of range
b'\x02\x99\x99\x00\n' reg index out of range
========
Instruction 3:
b'\x03\x00\x00\n' Thanks for playing
b'\x03\x04\x00\n' Thanks for playing
b'\x03\x08\x00\n' reg index out of range
b'\x03\x99\x00\n' reg index out of range
b'\x03\x04\x06\x00\n' Thanks for playing
b'\x03\x04\x99\x00\n' Unknown instruction at ip=0x2
b'\x03\x99\x06\x00\n' reg index out of range
b'\x03\x99\x99\x00\n' reg index out of range
========
Instruction 4:
b'\x04\x00\x00\n' Thanks for playing
b'\x04\x04\x00\n' Thanks for playing
b'\x04\x08\x00\n' reg index out of range
b'\x04\x99\x00\n' reg index out of range
b'\x04\x04\x06\x00\n' Thanks for playing
b'\x04\x04\x99\x00\n' Unknown instruction at ip=0x2
b'\x04\x99\x06\x00\n' reg index out of range
b'\x04\x99\x99\x00\n' reg index out of range
========
Instruction 5:
b'\x05\x00\x00\n' Thanks for playing
b'\x05\x04\x00\n' Thanks for playing
b'\x05\x08\x00\n' reg index out of range
b'\x05\x99\x00\n' reg index out of range
b'\x05\x04\x06\x00\n' Thanks for playing
b'\x05\x04\x99\x00\n' Unknown instruction at ip=0x2
b'\x05\x99\x06\x00\n' reg index out of range
b'\x05\x99\x99\x00\n' reg index out of range
========
Instruction 6:
b'\x06\x00\x00\n' Unknown instruction at ip=0x3
b'\x06\x04\x00\n' Unknown instruction at ip=0x3
b'\x06\x08\x00\n' reg index out of range
b'\x06\x99\x00\n' reg index out of range
b'\x06\x04\x06\x00\n' Thanks for playing
b'\x06\x04\x99\x00\n' Thanks for playing
b'\x06\x99\x06\x00\n' reg index out of range
b'\x06\x99\x99\x00\n' reg index out of range
========
Instruction 7:
b'\x07\x00\x00\n' Unknown instruction at ip=0x3
b'\x07\x04\x00\n' Unknown instruction at ip=0x3
b'\x07\x08\x00\n' Unknown instruction at ip=0x3
b'\x07\x99\x00\n' Unknown instruction at ip=0x3
b'\x07\x04\x06\x00\n' Thanks for playing
b'\x07\x04\x99\x00\n' reg index out of range
b'\x07\x99\x06\x00\n' Thanks for playing
b'\x07\x99\x99\x00\n' reg index out of range
========
Instruction 8:
b'\x08\x00\x00\n' Thanks for playing
b'\x08\x04\x00\n' Unknown instruction at ip=0x3
b'\x08\x08\x00\n' Thanks for playing
b'\x08\x99\x00\n' Unknown instruction at ip=0x1
b'\x08\x04\x06\x00\n' Thanks for playing
b'\x08\x04\x99\x00\n' reg index out of range
b'\x08\x99\x06\x00\n' Unknown instruction at ip=0x1
b'\x08\x99\x99\x00\n' Unknown instruction at ip=0x1
========
Instruction 9:
b'\t\x00\x00\n' Unknown instruction at ip=0x0
b'\t\x04\x00\n' Unknown instruction at ip=0x0
b'\t\x08\x00\n' Unknown instruction at ip=0x0
b'\t\x99\x00\n' Unknown instruction at ip=0x0
b'\t\x04\x06\x00\n' Unknown instruction at ip=0x0
b'\t\x04\x99\x00\n' Unknown instruction at ip=0x0
b'\t\x99\x06\x00\n' Unknown instruction at ip=0x0
b'\t\x99\x99\x00\n' Unknown instruction at ip=0x0
========
"""
