## Solution
A [LCG](https://en.wikipedia.org/wiki/Linear_congruential_generator) challenge, given by the formula:

$$
X_{n + 1} \equiv (a * X_n + b) \mod{m}
$$

where $0 \lt a \lt m$, $0 \leq c \lt m$. It's easily to see that:

$$
X_{n + 2} \equiv (a * X_{n + 1} + b) \mod{m}
$$

Subtracting them, we have

$$
X_{n+2} - X_{n+1} \equiv a * (X_{n+1} - X_{n}) \mod{m}
$$

and finally

$$
a \equiv (X_{n+2} - X_{n+1})^{-1} * (X_{n+1} - X_{n}) \mod{m}
$$


then $b$ is given by

$$
b \equiv X_{n+1} - (a * X_{n}) \mod{m}
$$


## Flag
```
LITCTF{wh47_1s_4n_lcgcg?_4_qu4dr4t1c_c0ngru3nt14l_g3nr4t0r?}
```