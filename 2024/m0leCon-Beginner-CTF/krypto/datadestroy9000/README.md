## Solution
Let's me bring the `scramble()` here:

```python
def scramble(block: bytes, perm: list):
    #scramble 32 bytes of a message given the permutation
    result = []
    for i in range(BLOCK_SIZE):
        result.append(block[perm[i]])
    return bytes(result)
```

After spending a while (roughly an afternoon, tho), I finally discovered that, `perm[i]` in `scramble()` function is a constant. This means we can try to manipulate the value of `data` to obtain `perm[i]`.    
My approach is as follow:     
1. Obtain the raw encrypted `otp`, by giving `\x00` as data to server, then split it into blocks of size 32 (4 blocks, cuz `CS // BS = 4`).
2. For each block, we need to determine its corresponding `permutation`.
3. To do so, iterate over all of its 32 position of indexes, append `\x01` as a suffix to an `i`-byte length block of `\x00`, give it to server, and obtain `c_test`.
4. Comparing the found `c_test` with the raw encrypted `otp`, check if there exists an index that have 2 different value. If so, store this index as our `perm[i]`.
5. Repeating this process across the 4 blocks, we find 4 permutations, each consisting of exactly 32 elements, with values ranging from 0 - 31.     

By gaining the `permutations`, we simply recover the actual `otp` by:   
```python
otp = []
for sub, oc in zip(subs, enc_otp):
    otp.append([oc[sub[i]] for i in range(BS)])
```

and also, the `flag`:
```python
flag = []
for perm, ec in zip(perms, enc_flag):
    flag.append([ec[perm[i]] for i in range(BS)])
```
Final step is just XOR-ing:
```python
print(xor(otp, flag))
```

I solved this challenge after the competition ended up, so there is no flag found :(((      
_-tysm for reading-_