# m0leCon Beginner CTF
<br>

## Small RSA
<br>

## Approach
Because `n` is hidden, we can find `n` by sending different `x` values to server, and receive the `r` remainders of them. Then find `gcd` of all `x - r`.
```python
e = 0x10001
#r1, r2, r3 are received from server
r1 = pow(2, e, n)
r2 = pow(3, e, n)
r3 = pow(5, e, n)
m1 = pow(2, e)
m2 = pow(3, e)
m3 = pow(5, e)
n = gcd([m1 - r1, m2 - r2, m3 - r3])
```
Now, the task is find `p`.    
Cuz we cannot send a number that greater than `p` to server, we can use binary search to find it. Remember that if `a = b * c`, then `b <= sqrt(a)`.
```python
l, r = 0, int(sqrt(n))
p = (l + r) // 2
    while l < r:
        io.sendlineafter(b"> ", b"1")
        io.sendlineafter(b"hex: ", long_to_bytes(p).hex().encode())
        recv = io.recvlinesS(3)
        if "b'Error: message to encrypt is too big'" in recv:
            l, r = l, p - 1
            p = (l + r) // 2
        else:
            l, r = p + 1, r
            p = (l + r) // 2
```
Cuz `flag < p`, then:
$$flag\ (\textrm{mod}\ n) \equiv \ flag \ (\textrm{mod}\ p)$$
$$\implies c^d\ (\textrm{mod}\ n) \equiv \ c^d (\textrm{mod}\ p)$$
$$where:\;\;e*d \equiv 1 \ (\ \textrm{mod}\ \phi(p)\ )$$
```python
d = pow(e, -1, p - 1)
flag = long_to_bytes(pow(ct, d, p))
```