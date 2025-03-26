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
