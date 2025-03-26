# m0leCon Beginner CTF

## Droid Cryptor

> ...

## Approach

Code the decryption logic in Java.

```java
import javax.crypto.*;
import javax.crypto.spec.GCMParameterSpec;
import javax.crypto.spec.SecretKeySpec;
import java.util.Base64;

public class Test {
    private static final String IV = "TXdESVBYeWc1dldkbHNFaQ==";
    private static final String Key = "YWYwYjAyYjkzNmRhZjU3Yg==";
    private static final String Output = "XZdGZ7pi9Ih4wHL/8Mj0q8/o6i/utS2tIsigHXCaEzpTXgesqtnLNJMbagqYH67ut9dbxhXC28w=";

    public static String decrypt() throws Exception {
        Base64.Decoder decoder = Base64.getDecoder();
        SecretKey secretKey = new SecretKeySpec(decoder.decode(Key), "AES");
        GCMParameterSpec gcmParameterSpec = new GCMParameterSpec(128, decoder.decode(IV));
        Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding");
        cipher.init(Cipher.DECRYPT_MODE, secretKey, gcmParameterSpec);
        byte[] decryptedData = cipher.doFinal(decoder.decode(Output));
        return new String(decryptedData);
    }

    public static void main(String[] args) throws Exception {
        String decryptedData = decrypt();
        System.out.println("Decrypted Data: " + decryptedData);
    }
}
```

## Flag

```
ptm{th3nk_y0u_f0r_r3st0r1ng_mY_m3ss4g3!}
```
