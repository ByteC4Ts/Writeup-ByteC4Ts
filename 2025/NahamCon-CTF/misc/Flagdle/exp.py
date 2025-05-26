import requests

url = "http://challenge.nahamcon.com:32089/guess"


# 🟩 = correct letter, correct position
# 🟨 = correct letter, wrong position
# ⬛ = incorrect letter
def guess(flag):
    resp = requests.post(url, json={"guess": flag})
    result = resp.json()["result"]
    return result


flag_int = 0
for ch in "0123456789abcdef":
    result = guess("flag{" + ch * 32 + "}")
    print(result)
    for i in range(len(result)):
        if result[i] == "🟩":
            flag_int |= (int(ch, 16) << (31 - i) * 4)

print(f"flag{{{hex(flag_int)[2:]}}}")

# flag{bec42475a614b9c9ba80d0eb7ed258c5}
