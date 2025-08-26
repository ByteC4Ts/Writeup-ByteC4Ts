## Solution
In this challenge $k$ is just 32-bit length. Assume that $k$ is not a prime, so we can represent $k$ as $k = a * b$, where $a \in [0, 2^{16}]$.  


We are given 3 attributes, called $n, e, c$. The encryption formula can be written as follow:

$$
ck \equiv k^e \equiv (a*b)^e \mod{n}
$$

or

$$
ck * a^{-e} \equiv b^e \mod{n}
$$

Because $a \in [0, 2^{16}]$, it is feasible to bruteforce $a$. Then compute the value of $ck * a^{-e} \mod{n}$, store this value into a lookup table.     
Assume that $a$ is a 12 to 16-bit length, then we can reduce the range of $b$ to $[2^{16}, 2^{20}]$. Thus, compute $b^e \mod{n}$ and find it in our lookup table.


## Flag
```
INTIGRITI{w3_sh0uld_m33t_1n_th3_m1ddl3}
```