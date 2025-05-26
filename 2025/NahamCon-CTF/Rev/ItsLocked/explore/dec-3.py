import subprocess

# str="$(echo "$C" | openssl enc -d -aes-256-cbc -md sha256 -nosalt -k "C-${S}-${_P}" -a -A 2>/dev/null)"

S = "lRwuwaugBEhK488I"
C = "3eOcpOICWx5iy2UuoJS9gQ=="
_P = "QHh4K9JfgoACd2f4"  # from dec-2.py

cmd = f'echo "{C}" | openssl enc -d -aes-256-cbc -md sha256 -nosalt -k "C-{S}-{_P}" -a -A'
result = subprocess.run(cmd, shell=True, capture_output=True)

print(result)
print(result.stdout)  # b'R=2105\n\n'
