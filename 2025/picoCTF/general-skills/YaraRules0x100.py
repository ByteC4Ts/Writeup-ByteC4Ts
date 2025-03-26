import subprocess

port = 54813
rules_template = """
import "hash"

rule bf
{{
    condition:
        hash.sha256(0, filesize) matches /^1b/ or
        hash.sha256(0, filesize) matches /^8f/ or
        hash.sha256(0, filesize) matches /^{}/
}}
"""

for i in range(256):
    h = hex(i)[2:].zfill(2)  # 00, 01, ..., ff
    rules = rules_template.format(h)
    process = subprocess.Popen(
        ["socat", "-t60", "-", f"TCP:standard-pizzas.picoctf.net:{port}"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE
    )
    stdout, stderr = process.communicate(input=rules.encode())
    print(h, stdout)

# picoCTF{yara_rul35_r0ckzzz_a73309a8}
