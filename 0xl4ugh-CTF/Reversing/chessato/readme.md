# 0xl4ugh CTF

## chessato

> We will be playing chess, but with my own rules. Can you beat me in 1 move?

## Approach

Using dnSpy to decompile the file `Managed/Assembly-CSharp.dll`, we can see the decryption logic in the `Winner` method of the `Game` class:

![1.jpg](1.jpg)

In this process, `F1`, `F2` and `RM` perform some calculations on the input array to ultimately derive the `key` and `iv`, and the `FW` method performs AES decryption. The logic of these functions is simple, and I rewrite them in Python in the exploit scripts.

Similarly, in the `Winner` method, we can observe that `array` and `array2` represent the board states of the white and black sides:

![2.jpg](2.jpg)

Therefore, the next step is to obtain a board state that can be correctly used for decryption. Playing this chess game, the rules are customized: if we (the white side) have any pieces crossing the second row, they will be captured by the black side's pieces. If there are no white pieces above the second row, the black king will directly capture our king.

![3.jpg](3.jpg)

The challenge specifies "beat me in 1 move", which implies that the board state won't differ significantly from the initial state. This part was somewhat guessy for me. At first, I spent a long time trying to modify the initial position of the black king so that my pawn or knight could capture it in one move, but after winning I always get "Not Good Enough".

Then I attempted some bruteforce enumeration strategies. One of them was based on the observation that our pieces always get replaced by the opponent's pieces when they move beyond the second row. I tried setting the initial states of the white pieces to `0` one by one, and eventually discovered that the board state used for decryption is to set the white king to `0`.

In the official writeup, it is explained that we need to make the white king capture the black king in one move, just as the black king would directly capture the white king.

```python
from Crypto.Cipher import AES
import base64


def f1(matrix):
    array = bytearray(32)
    num = 0
    for i in range(8):
        for j in range(8):
            if num < len(array):
                array[num] = (matrix[j][i] * 16 + j + i) & 0xFF
                num += 1
    return bytes(array)


def f2(matrix):
    array = bytearray(16)
    num = 0
    for i in range(8):
        for j in range(8):
            if num < len(array):
                array[num] = (matrix[j][i] * 2 + j % 2 + i % 2) & 0xFF
                num += 1
    return bytes(array)


def rm(original_matrix):
    length = len(original_matrix)
    rotated_matrix = [[0] * length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            rotated_matrix[j][i] = original_matrix[length - 1 - j][length - 1 - i]
    return rotated_matrix


def fw(cipher_text, key, iv):
    cipher_bytes = base64.b64decode(cipher_text)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(cipher_bytes)
    return decrypted_data


array1 = [
    [3, 6, 0, 0, 0, 0, 0, 0],
    [5, 6, 0, 0, 0, 0, 0, 0],
    [4, 6, 0, 0, 0, 0, 0, 0],
    [2, 6, 0, 0, 0, 0, 0, 0],
    [0, 6, 0, 0, 0, 0, 0, 0],
    [4, 6, 0, 0, 0, 0, 0, 0],
    [5, 6, 0, 0, 0, 0, 0, 0],
    [3, 6, 0, 0, 0, 0, 0, 0],
]
array2 = [
    [0, 0, 0, 0, 0, 0, 6, 3],
    [0, 0, 0, 0, 0, 0, 6, 5],
    [0, 0, 0, 0, 0, 0, 6, 4],
    [0, 0, 0, 0, 0, 0, 6, 2],
    [0, 0, 0, 0, 0, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 6, 4],
    [0, 0, 0, 0, 0, 0, 6, 5],
    [0, 0, 0, 0, 0, 0, 6, 3],
]
cipher_text = "LlfqPs1MOul1Jr09d6dZditrkXUgIfMDc3Lh6/z5Ufv6E2G8ARHNvE7xQ9jrGBRg"

key = f1(array1)
matrix = rm(array2)
iv = f2(matrix)

decrypted_text = fw(cipher_text, key, iv)
print(decrypted_text)  # b'0xL4ugh{A_H0n0ur4ble_B4tt13_B3tw33n_K1NG5}\x06\x06\x06\x06\x06\x06'
```

## Flag

```
0xL4ugh{A_H0n0ur4ble_B4tt13_B3tw33n_K1NG5}
```
