# Proto Proto 2

## Approach

In summary, command `\x02\x15super_secret_password\x08flag.txt` conforms to the format of:

- `\x02[key_length][key][filename_length][filename]`

The key is circularly xor-ed with the flag.

```python
import socket

host = "chals.swampctf.com"
port = 44255

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp_socket.sendto(b"\x00", (host, port))
resp, addr = udp_socket.recvfrom(1024)
print(f"Received from {addr}:")  # Received from ('34.72.68.85', 44255):
print(resp)  # b'\x00\x02\x00\x00\x00\x01\x08\x00\x00\x00flag.txt\x01\r\x00\x00\x00real_flag.txt'


def send(data):  # make my life easier
    udp_socket.sendto(data, (host, port))
    resp = udp_socket.recv(1024)
    return resp


print(send(b"\x01super_secret_password"))  # b'\x01'

print(send(b"\x02\x15super_secret_password\x08flag.txt"))  # b'\x07i]ug]nBBt@0-\x0c]u30._)9U$@B0HM8\tH?HC9Ni*e\x0b'

# the key is circularly xor-ed with the flag
resp_password = send(b"\x02\x15super_secret_password\x08flag.txt")
resp_ff = send(b"\x02\x15" + b"\x00" * 21 + b"\x08flag.txt")
print(bytes([x ^ y for x, y in zip(resp_password, resp_ff)]))  # b'\x00super_secret_passwordsuper_secret_passwo'

print(send(b"\x02\x09swampCTF{\x08flag.txt"))  # b'\x07i_do_realA"8>]W\x14\x05"C,<K!ss\x04lM*\x0bW*\x7fH\x0fTi.s\t'

# guess the rest of the key should be "_encryption"
print(send(b"\x02\x14i_do_real_encryption\x08flag.txt"))  # b'\x07swampCTF{m070_m070_54y5_x0r_15_4_n0_n0}\n'

print("=" * 32)

print(send(b"\x02\x14i_do_real_encryption\x0dreal_flag.txt"))  # b'\x07https://hackback.zip\n'
```
