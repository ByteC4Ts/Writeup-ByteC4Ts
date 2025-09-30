## Solution
I've tried giving the server the data in `voyager.bin`, and it was authenticated, i.e, the plaintext was one of those `[0x13371337, 0x1337babe, 0xdeadbeef, 0xdeadbabe]`, which is encrypted after being packed in little endian unsigned integer order.   
Since the initial vector is given, and the plaintext space was just 4, we can bruteforce the plaintext, and forge the ciphertext by using [bit flipping attack](https://en.wikipedia.org/wiki/Bit-flipping_attack).     
Our aim is to make a forgery of `0xdeadbabe` device' ID.
## Flag
```
sun{m4yb3_4_ch3ck5um_w0uld_b3_m0r3_53cur3}
```