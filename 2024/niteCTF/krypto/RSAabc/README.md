# niteCTF
<br>

## RSAabc
<br>

## Approach
#### Challenge analysis:
Function `reverse_alphabet()` maps a character to its corresponding symmetric character in the alphabet, i.e: `reverse_alphabet('m') = 'n'`. The special case, when `char in ['{', '}', '_']`, the result `reverse_alphabet(char) = 'e'`.
```python
def reverse_alphabet(char):
    if char.isupper():
        return chr(155 - ord(char))
    elif char.islower():
        return chr(219 - ord(char))
    elif char == "_" or "{" or "}":
        return "e"
```
Only character has `ord()` is not a prime number will be mapped using `reverse_alphabet()` function.
```python
if not sp.isprime(ord(ch)):
    transformed_char = reverse_alphabet(ch)
    file1.write(transformed_char)
```
All values of `n` in `range(2**1029, 2**1049)`, but `p` only in `range(2**5, 2**25)`, feasbile to factor `n` and compute `inverse_mod(e)`.
```python
pre = ord(ch) % 26
if pre < 5:
    pre += 5
p = getPrime(pre)
q = getPrime(1024)
n = p * q

#factor and compute euler_phi
def mod_inv(inp):
res = []
for n in inp:
    fs = list(factor(n))
    fs = [(p ** (e - 1) * (p - 1)) for p, e in fs]
    res += [prod(fs)]
return [pow(0x10001, -1, phi) for phi in res]
```
All values of `lan` are obtained through `language` dictionary with the key `eng`. So, we can recover `eng` by `lan` through a `trans` dictionary.
```python
trans = {'A': 'Α', 'a': 'α', 'B': 'Β', 'b': 'β', 'S': 'Σ', 'c': 'σ', 'D': 'Δ', 'd': 'δ', 'E': 'Ε', 'e': 'ε', 'F': 'Φ', 'f': 'φ', 'G': 'Γ', 'g': 'γ', 'H': 'Η', 'h': 'η', 'I': 'Ι', 'i': 'ι', 'J': 'Ξ', 'j': 'ξ', 'K': 'Κ', 'k': 'κ', 'L': 'Λ', 'l': 'λ', 'M': 'Μ', 'm': 'μ', 'N': 'Ν', 'n': 'ν', 'O': 'Ο', 'o': 'ο', 'P': 'Π', 'p': 'π', 'Q': 'Θ', 'q': 'θ', 'R': 'Ρ', 'r': 'ρ', 's': 'ς', 'T': 'Τ', 't': 'τ', 'Y': 'Υ', 'y': 'υ', 'V': 'Ω', 'v': 'ω', 'W': 'Ψ', 'w': 'ψ', 'X': 'Χ', 'x': 'χ', 'Z': 'Ζ', 'z': 'ζ'}
eng = trans.get(lan)
```
#### Recover flag:    
All `ascii` characters in `ciphertext` can be recovered by using the function `reverse_alphabet()`, but `'e'`, we will map `'e'` into `'_'`, and modify the final result manually to match the form of flag `nite{...}`.
```python
def reverse_char(char):
    if char == "e":
        return "_"
    if char.isupper():
        return chr(155 - ord(char))
    elif char.islower():
        return chr(219 - ord(char))
```
Because `xor` does not change _bit-length_, so we can recover original `ciphertext` like follow:
```python
def googly(number, position):
    mask = 1 << position
    return number ^ mask
c = googly(c, c.bit_length() - ord(eng)) #eng is obtained as above
```
Now both original `ciphertext` and its corresponding `inverse_mod(e)` are in reached, decipher and get `flag`.
```python
pt += [chr(pow(c, ds[i], ns[i]))]
print(''.join(pt))
```

## Flag
```
nite{quICklY_grab_the_codE5_sgOqkA}
```