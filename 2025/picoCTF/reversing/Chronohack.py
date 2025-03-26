import socket
import random
import time

port = 50408
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("verbal-sleep.picoctf.net", port))

t1 = int(time.time() * 1000)
data = s.recv(1024)
print(data.decode())
t2 = int(time.time() * 1000)


def get_random(length):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    random.seed(random.randint(t1, t2))
    s = ""
    for i in range(length):
        s += random.choice(alphabet)
    return s


n = 0
while n < 50:
    user_guess = get_random(20)
    s.sendall(user_guess.encode() + b"\n")
    response = s.recv(1024)
    print(response.decode())
    n += 1

s.close()

# picoCTF{UseSecure#$_Random@j3n3r@T0rsb5f8a5af}
