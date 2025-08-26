## Solution
Server only accepts large exponent $x$ such as $x^2 \ge 996491788296388609$, meaning that negative value is acceptable. We give a pair of value ${k + 1, -k}$ to server and receive a pair of remainders such as:

$$
\begin{cases}
r_1 \equiv a^{k+1} \mod{n} \\
r_2 \equiv a^{-k} \mod{n}
\end{cases}
$$

Multiplying $r_1$ and $r_2$, we get,

$$
r_1 * r_2 \equiv a^{k + 1} * a^{-k} \equiv a \mod{n}
$$

Similarly,

$$
\begin{cases}
r_3 * r_4 \equiv a^{k + 3} * a^{-k - 2} \equiv a \mod{n} \\
r_5 * r_6 \equiv a^{k + 5} * a^{-k - 4} \equiv a \mod{n} \\
r_7 * r_8 \equiv a^{k + 7} * a^{-k - 6} \equiv a \mod{n} \\
\end{cases}
$$

Subtracting $r_1 * r_2$ from $r_3 * r_4$, we have,

$$
r_3 * r_4 - r_1 * r_2 \equiv 0 \mod{n}
$$

that is,

$$
t_1 = r_3 * r_4 - r_1 * r_2 = k_1 * n
$$

similarly,

$$
t_2 = r_7 * r_8 - r_5 * r_6 = k_2 * n
$$


Because both $k_1 * n$ and $k_2 * n$ could be even, we need to factorize $gcd(t_1, t_2)$, the largest one is $n$.

## Flag
```
LITCTF{GCD_GREATEST_892066f8}
```