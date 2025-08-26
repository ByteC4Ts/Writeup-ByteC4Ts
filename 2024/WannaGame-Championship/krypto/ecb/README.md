## Solution
After checking on [Pypi: gostcrypto](https://pypi.org/project/gostcrypto/), I've found that the challenge used AES-ECB mode.   
Each time we send plaintext to server, $flag$ is added as a suffix of plaintext. However, the $key$ is reused for encryption process, we purely exploit this attribute. As in ECB mode, each block is encrypted independently, meaning the same input block always produces identical cipher block.     
According to the above property of ECB, we can recover the $flag$ without $key$ by using a technique called _Byte at a time_.       
Firstly, to recover the first byte of $flag$, we need to send a $payload$ which has a length of $16*n + 15$ in order to make the flag's 1st byte concats as the last byte of plaintext block. Obtain $16*(n+1)$ first bytes of server-returned ciphertext, save it as $pattern$. Then iterating over 255 bytes, or just `string.printable` set in case of CTF, concat our $payload$ with this byte and send to server. In each iteration, obtain $16*(n+1)$ first bytes of the ciphertext, compare it with $pattern$, if they are identical, then we've found the first byte of $flag$. 
Repeatedly, by decreasing the $payload$ length, we found the second byte, the third byte,... and the entire $flag$.
>Note: from the second byte, we have to concat payload with flag_segment (found bytes) and finally experiment byte before sending to server. 

See more detail here: [Byte At A time ECB Attack](https://crypto.stackexchange.com/questions/87666/byte-at-a-time-ecb-attack).


## Flag
```
W1{0Ld_pr0bl3m_BUT_n3W_c1pher}
```