# m0leCon Beginner CTF

## Cookie Shop

> https://cookieshop.challs.m0lecon.it/

## Approach

Just update the cookie. You can type `btoa('{"balance": 99999}')` in the console to get the base64 encoded value of the cookie.

```
> btoa('{"balance": 99999}')
< 'eyJiYWxhbmNlIjogOTk5OTl9'
```

## Flag

```
ptm{d0_y0u_w4nt_4_co0k13????}
```
