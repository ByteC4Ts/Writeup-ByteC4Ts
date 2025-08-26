## Solution
So the `seed` is in `range(10000)`, which is feasible to bruteforce. All we need to do is just generating the `tokens` list containing 1337 another list, each has some random element from 0 to 254, reverse the `tokens` and XOR with ciphertext.


## Flag
```
W1{maybe_the_seed_is_too_small..._b32fe938a402c22144b9d6497fd5a709}
```