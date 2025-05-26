import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("challenge.nahamcon.com", 32543))

s.send(b"\n" * 1000)
for i in range(1000):
    print(s.recv(1024))

# flag{0b51aae6b09b85d1bb13b0b8c3003a6a}
