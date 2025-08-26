## Solution
Mah teammate [@1kuzus](https://github.com/1kuzus) said that this challenge is a [Uniform distribution](https://en.wikipedia.org/wiki/Discrete_uniform_distribution) based challenge. So the probabilities for both `0` and `1` are the same (equal to 0.5, particularly). Counting the appearances of each bit in the given ciphertext, allows us determine the probability of the next bit by comparing the `found_prob` with 0.5.     
Then we found this kind of readable string:
```
L\xc9TC\xd4F{n0t_4_c0!n[FliP...c66f2b}
```
And the sticky note from author:
```
If you see a !, replace it with a 1. If you see a [, replace it with a _.
Also, the flag should have one lowercase f. If you see two, replace the first with an F.
```
## Flag
```
LITCTF{n0t_4_c01n_FliP..c66f2b}
```