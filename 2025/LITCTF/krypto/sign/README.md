## Solution
Absolutely straightforward due to the fact that `padded_flag` is being encrypted with private exponent `d`. Then just `pow(padded, e, n)` to recover flag.

## Flag
```
LITCTF{1m_s34ch1ng_f0r_4_n3w_h4sh1ng_func710n}
```