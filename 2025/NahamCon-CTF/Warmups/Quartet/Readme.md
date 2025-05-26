# Quartet

## **Challenge description**

```
Ah, a quartet is a collection of its unique and individuals parts... and together, this has all my favorite kinds of instruments!
```

```
Attachements: quartet.z01  quartet.z02  quartet.z03  quartet.z04
```

## **Solve**

- We start by checking the files type.

```sh
file *


quartet.z01: Zip multi-volume archive data, at least PKZIP v2.50 to extract

quartet.z02: data

quartet.z03: data

quartet.z04: Zip archive data, made by v3.0 UNIX, extract using at least v2.0, last modified, last modified Sun, May 10 2025 04:28:04, uncompressed size 2035495, method=deflate
```

- We notice we have some zip files.
- We extract the first one with `7z` and find an image `quartet.jpeg`.

```sh
7z x quartet.z01 
```

- We simply find the flag in the image metadata using `strings`.

```sh
strings quartet.jpeg | grep flag

flag{8f667b09d0e821f4e14d59a8037eb376}
```



