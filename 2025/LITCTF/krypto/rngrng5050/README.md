## Solution
Mah teammate [@1kuzus](https://github.com/1kuzus) said that this related to [ratio distribution of 2 independent uniform distribution](https://stats.stackexchange.com/questions/185683/distribution-of-ratio-between-two-independent-uniform-random-variables). The fact that the probability of generating bit `1` is a bit larger than generating bit `0` (i.e, ~0.535). Then in a sample of `1000` _random-generated_ bit, the amount of bit `1` must be greater than 500, we literally take advantage of this property to determine whether the next _random-generated_ bit is `1` or `0`.     
After doing some statistical tasks, we found out this kind of "readable" string:
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