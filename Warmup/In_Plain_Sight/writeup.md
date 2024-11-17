# 1337Up Live CTF
## In Plain Sight
Barely hidden tbh..
## Approach
We find that we are given a jpg image file called meow.jpg
Running it through `binwalk`, there is a compressed zip archive with a password in it. 

![a1e030e97bb1a99d61f02af54636971a.png](:/92013c7790dc442e940a4b814d1c5c42)

We have an encrypted Zip file but no password now

![254c625fed47f8a1bd3bd701cc903b2a.png](:/f1fa26aa56184545bc2ae3e8279869c9)
Running the `meow.jpg` through strings we find something interesting 

![5c74818bdbc6db617ada084d2530f145.png](:/e4b21538b08b4b42a2650736047bd49b)
Trying `YoullNeverGetThis719482`  as the password we are able to sucessfully decrypt it. 
We get a file called `flag.png` which is completely blank
![bcaea2f96c3ecccd2187a1fc31e8936c.png](:/9c2318c5ae6e4b78afe0033542e94efb)

Uploading the `flag.png` to `https://aperisolve.com` we are able to view the [flag](https://www.aperisolve.com/ed9edd995a595a8a6e359ec6719ede98)
![06f18c508019e808c0f7145998fb323a.png](:/be8191c10d1b45278bbb47a3c6bc8a25)

## The Flag is: 
```
INTIGRITI{w4rmup_fl46z}
```

