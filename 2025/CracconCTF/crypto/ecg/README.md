## Solution
An collaboration of RSA cryptosystem and [LCG](https://en.wikipedia.org/wiki/Linear_congruential_generator). We have to recover `n, s0, c, m` in order to recover flag.     

### Solving LCG stuff
Let me re-write LCG formula here:

$$
X_{k+1} \equiv a * X_k + c \mod{n}
$$

In this challenge, `m` is not given, so we need to recover `m` first. The fact that,

$$
\begin{cases}
X_2 - X_1 \equiv a * (X_1 - X_0) \mod{n} \\
X_3 - X_2 \equiv a * (X_2 - X_1) \mod{n}
\end{cases}
$$

so we have,

$$
(X_2 - X_1) * (X_1 - X_0)^{-1} \equiv (X_3 - X_2) * (X_2 - X_1)^{-1} \mod{n}
$$

multiply each side by the value of $(X_1 - X_0) * (X_2 - X_1)$,

$$
(X_2 - X_1)^2 \equiv (X_3 - X_2) * (X_1 - X_0) \mod{n}
$$

implies that,

$$
t_1 = (X_2 - X_1)^2 - (X_3 - X_2) * (X_1 - X_0) = k_1 * n
$$

similarly we found $t_2$,

$$
t_2 = (X_3 - X_2)^2 - (X_4 - X_3) * (X_2 - X_1) = k_2 * n
$$

then $\gcd(t_1, t_2)$ can be a multiple of $n$, factor it and $n$ is the largest one. Once we obtained value of $n$, $a$ could be found by the following formula:

$$
a \equiv (X_1 - X_0)^{-1} * (X_2 - X_1) \mod{n}
$$

and $b$ is given by:

$$
b \equiv X_1 - (X_0 * a) \mod{n}
$$


### Solving RSA stuff
This stuff is quite weird cuz $e$ is chosen to be not coprime with $\phi(n)$, so, traditional RSA decryption progress does not make sense. I found out [this blog](https://medium.com/@g2f1/bad-rsa-keys-3157bc57528e) given an approach to solve this kind of issue. As represented is the blog,
1. The group of units of the integers modulo $n$ can be written as $Z_n^* = E \times G$ where $|E| = k$ and $|G| = \frac{\phi(n)}{k}$ where $k$ is an integer such that $\gcd(e, \phi(n)) = 1$.
2. Because $m \in Z_n^*$, then $m$ can be represented as $m = g * l$ for $(g, l) \in E \times G$.
3. Then $c \equiv m^e \equiv (g * l)^e \equiv g^e * l^e \equiv g^e \mod{n}$. 
Our mission is finding these kind of $l \in G$, they are called _e-th_ [roots of unity](https://en.wikipedia.org/wiki/Root_of_unity_modulo_n) modulo $n$.


Since $\gcd(e, \frac{\phi(n)}{k}) = 1$, there exists an integer $d$ such that $e * d \equiv 1 \mod{\frac{\phi(n)}{k}}$. So,

$$
c^d \equiv g^{e*d} \equiv g^{\alpha * \frac{\phi(n)}{k}} \equiv g \mod{n}
$$




## Flag
```
craccon{Y0U_CR4CK3D_3CG!}
```