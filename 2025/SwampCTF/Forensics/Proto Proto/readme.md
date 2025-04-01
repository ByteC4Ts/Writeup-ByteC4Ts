# Proto Proto

## Approach

After analyzing the UDP frames in `proto_proto.pcap`, there are two important "custom commands":

- `\x00`: This will list the files in the directory. We get `b'\x00\x01\x00\x00\x00\x01\x08\x00\x00\x00flag.txt'`.

- `\x02\x08flag.txt`: This will return the content of the file `flag.txt`, note that `\x08` is the length of the filename `"flag.txt"`.

```python
import socket

host = "chals.swampctf.com"
port = 44254

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp_socket.sendto(b"\x00", (host, port))
resp, addr = udp_socket.recvfrom(1024)
print(f"Received from {addr}:")  # Received from ('34.72.68.85', 44254):
print(resp)  # b'\x00\x01\x00\x00\x00\x01\x08\x00\x00\x00flag.txt'

udp_socket.sendto(b"\x02\x08flag.txt", (host, port))
resp = udp_socket.recv(1024)
print(resp)  # b'\x07swampCTF{r3v3r53_my_pr070_l1k3_m070_m070}\n'

udp_socket.close()

# swampCTF{r3v3r53_my_pr070_l1k3_m070_m070}
```
