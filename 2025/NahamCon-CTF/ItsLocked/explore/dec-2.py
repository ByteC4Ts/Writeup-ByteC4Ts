import subprocess

# _k="$(_bcl_get)" && _P="$(echo "$1" | openssl enc -d -aes-256-cbc -md sha256 -nosalt -k "$_k" -a -A 2> /dev/null)";

P = "llLvO8+J6gmLlp964bcJG3I3mY27I9ACsJTvXYCZv2Q="
_k = "hello-1338"  # from dec-1.py

cmd = f'echo "{P}" | openssl enc -d -aes-256-cbc -md sha256 -nosalt -k "{_k}" -a -A'
result = subprocess.run(cmd, shell=True, capture_output=True)

print(result)
print(result.stdout)  # b'QHh4K9JfgoACd2f4\n'
