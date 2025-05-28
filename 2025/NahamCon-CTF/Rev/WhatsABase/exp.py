# findings
# length: 5n -> 8n
# custom base32 alphabet: ybndrfg8ejkmcpqxot1uwisza345h769

# tests
# 00000 -> gyadycbo
# 00001 -> gyadycbt
# 11111 -> grauncjt
# aaaaa -> cfosnamb

# target
# ??? -> m7xzr7muqtxsr3m8pfzf6h5ep738ez5ncftss7d1cftskz49qj4zg7n9cizgez5upbzzr7n9cjosg45wqjosg3mu

import base64

b32_alphabet = "abcdefghijklmnopqrstuvwxyz234567"
custom_base32_alphabet = "ybndrfg8ejkmcpqxot1uwisza345h769"
table_enc = str.maketrans(b32_alphabet, custom_base32_alphabet)
table_dec = str.maketrans(custom_base32_alphabet, b32_alphabet)


def custom_base32_encode(data):
    result = base64.b32encode(data)
    result = result.decode().lower()
    return result.translate(table_enc)


def custom_base32_decode(result):
    result = result.translate(table_dec)
    result = result.encode().upper()
    data = base64.b32decode(result)
    return data


print(custom_base32_encode(b"00000"))  # gyadycbo
print(custom_base32_encode(b"aaaaa"))  # cfosnamb

print(custom_base32_decode("gyadycbo"))  # b'00000'
print(custom_base32_decode("cfosnamb"))  # b'aaaaa'

target = "m7xzr7muqtxsr3m8pfzf6h5ep738ez5ncftss7d1cftskz49qj4zg7n9cizgez5upbzzr7n9cjosg45wqjosg3mu"
print(custom_base32_decode(target))  # __rust_begin_short_backtrace__rust_end_short_backtraces

# Congratulations! flag{50768fcb270edc499750ea64dc45ee92}
