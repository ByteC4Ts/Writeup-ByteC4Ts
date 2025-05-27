# It's Locked

```
This bin looks locked as a crypt to me, but I'm sure you can work some magic here.
All I know is that this came from a machine with a cryptic ID of just 'hello'.
```

## Approach

The given `flag.sh` script contains a lot of unreadable binary or non-printable characters. But we can still barely recognize the following part:

![1.jpg](1.jpg)

Which is:

```sh
LANG=C perl -pe "s/[^print:]//g" | openssl base64 -A -d
```

And `s/[^print:]//g` means to remove all non-printable characters, which inspires us to extract the printable characters from the script. We use the following script:

```python
with open("flag.sh", "rb") as f:
    content = f.read()

simplified = b""

for ch in content:
    if 32 <= ch <= 126:
        simplified += bytes([ch])

with open("flag_simplified.sh", "wb") as f:
    f.write(simplified)
```

And get `flag_simplified.sh` which includes a long Base64 string. We can decode it into the following content:

```sh
_bcl_verify_dec ()
{
    [ "TEST-VALUE-VERIFY" != "$(echo "$BCV" | openssl enc -d -aes-256-cbc -md sha256 -nosalt -k "B-\${1}-\${UID}" -a -A 2> /dev/null)" ] && return 255;
    echo "$1-\${UID}"
}
_bcl_verify() { _bcl_verify_dec "$@"; }
_bcl_get ()
{
    [ -z "$UID" ] && UID="$(id -u 2> /dev/null)";
    [ -f "/etc/machine-id" ] && _bcl_verify "$(cat "/etc/machine-id" 2> /dev/null)" && return;
    command -v dmidecode > /dev/null && _bcl_verify "$(dmidecode -t 1 2> /dev/null | LANG=C perl -ne '/UUID/ && print && exit')" && return;
    _bcl_verify "$({ ip l sh dev "$(LANG=C ip route show match 1.1.1.1 | perl -ne 's/.*dev ([^ ]*) .*/\1/ && print && exit')" | LANG=C perl -ne 'print if /ether / && s/.*ether ([^ ]*).*/\1/'; } 2> /dev/null)" && return;
    _bcl_verify "$({ blkid -o export | LANG=C perl -ne '/^UUID/ && s/[^[:alnum:]]//g && print && exit'; } 2> /dev/null)" && return;
    _bcl_verify "$({ fdisk -l | LANG=C perl -ne '/identifier/i && s/[^[:alnum:]]//g && print && exit'; } 2> /dev/null)" && return;
}
_bcl_gen_p ()
{
    local _k;
    local str;
    [ -z "$BC_BCL_TEST_FAIL" ] && _k="$(_bcl_get)" && _P="$(echo "$1" | openssl enc -d -aes-256-cbc -md sha256 -nosalt -k "$_k" -a -A 2> /dev/null)";
    [ -n "$_P" ] && return 0;
    [ -n "$fn" ] && {
        unset BCL BCV _P P S fn;
        unset -f _bcl_get _bcl_verify _bcl_verify_dec;
        return 255
    };
    BCL="$(echo "$BCL" | openssl base64 -d -A 2> /dev/null)";
    [ "$BCL" -eq "$BCL" ] 2> /dev/null && exit "$BCL";
    str="$(echo "$BCL" | openssl base64 -d -A 2> /dev/null)";
    BCL="\${str:-$BCL}";
    exec /bin/sh -c "$BCL";
    exit 255
}
BCL='aWQgLXUK'
BCV='93iNKe0zcKfgfSwQoHYdJbWGu4Dfnw5ZZ5a3ld5UEqI='
P=llLvO8+J6gmLlp964bcJG3I3mY27I9ACsJTvXYCZv2Q=
S='lRwuwaugBEhK488I'
C=3eOcpOICWx5iy2UuoJS9gQ==
for x in openssl perl gunzip; do
    command -v "$x" >/dev/null || { echo >&2 "ERROR: Command not found: $x"; return 255; }
done
unset fn _err
if [ -n "$ZSH_VERSION" ]; then
    [ "$ZSH_EVAL_CONTEXT" != "\${ZSH_EVAL_CONTEXT%":file:"*}" ] && fn="$0"
elif [ -n "$BASH_VERSION" ]; then
    (return 0 2>/dev/null) && fn="\${BASH_SOURCE[0]}"
fi
fn="\${BC_FN:-$fn}"
XS="\${BASH_EXECUTION_STRING:-$ZSH_EXECUTION_STRING}"
[ -z "$XS" ] && unset XS
[ -z "$fn" ] && [ -z "$XS" ] && [ ! -f "$0" ] && {
    echo >&2 'ERROR: Shell not supported. Try "BC_FN=FileName source FileName"'
    _err=1
}
_bc_dec() {
    _P="\${PASSWORD:-$BC_PASSWORD}"
    unset _ PASSWORD
    if [ -n "$P" ]; then
        if [ -n "$BCV" ] && [ -n "$BCL" ]; then
            _bcl_gen_p "$P" || return
        else
            _P="$(echo "$P"|openssl base64 -A -d)"
        fi
    else
        [ -z "$_P" ] && {
            echo >&2 -n "Enter password: "
            read -r _P
        }
    fi
    [ -n "$C" ] && {
        local str
        str="$(echo "$C" | openssl enc -d -aes-256-cbc -md sha256 -nosalt -k "C-\${S}-\${_P}" -a -A 2>/dev/null)"
        unset C
        [ -z "$str" ] && {
            [ -n "$BCL" ] && echo >&2 "ERROR: Decryption failed."
            return 255
        }
        eval "$str"
        unset str
    }
    [ -n "$XS" ] && {
        exec bash -c "$(printf %s "$XS" |LANG=C perl -e '<>;<>;read(STDIN,$_,1);while(<>){s/B3/\n/g;s/B1/\x00/g;s/B2/B/g;print}'|openssl enc -d -aes-256-cbc -md sha256 -nosalt -k "\${S}-\${_P}" 2>/dev/null|LANG=C perl -e "read(STDIN,\$_, \${R:-0});print(<>)"|gunzip)"
    }
    [ -z "$fn" ] && [ -f "$0" ] && {
        zf='read(STDIN,\$_,1);while(<>){s/B3/\n/g;s/B1/\\x00/g;s/B2/B/g;print}'
        prg="perl -e '<>;<>;$zf'<'\${0}'|openssl enc -d -aes-256-cbc -md sha256 -nosalt -k '\${S}-\${_P}' 2>/dev/null|perl -e 'read(STDIN,\\\$_, \${R:-0});print(<>)'|gunzip"
        LANG=C exec perl '-e$^F=255;for(319,279,385,4314,4354){($f=syscall$_,$",0)>0&&last};open($o,">&=".$f);open($i,"'"$prg"'|");print$o(<$i>);close($i)||exit($?/256);$ENV{"LANG"}="'"$LANG"'";exec{"/proc/$$/fd/$f"}"'"\${0:-python3}"'",@ARGV' -- "$@"
    }
    [ -f "\${fn}" ] && {
        unset -f _bcl_get _bcl_verify _bcl_verify_dec
        unset BCL BCV _ P _err
        eval "unset _P S R fn;$(LANG=C perl -e '<>;<>;read(STDIN,$_,1);while(<>){s/B3/\n/g;s/B1/\x00/g;s/B2/B/g;print}'<"\${fn}"|openssl enc -d -aes-256-cbc -md sha256 -nosalt -k "\${S}-\${_P}" 2>/dev/null|LANG=C perl -e "read(STDIN,\$_, \${R:-0});print(<>)"|gunzip)"
        return
    }
    [ -z "$fn" ] && return
    echo >&2 "ERROR: File not found: $fn"
    _err=1
}
[ -z "$_err" ] && _bc_dec "$@"
unset fn
unset -f _bc_dec
if [ -n "$_err" ]; then
    unset _err
    false
else
    true
fi
```

`_bcl_get` function tries a series of machine-unique identifiers to generate a key, and then decrypts the `BCV` variable using the key. And this challenge gives us an important hint:

> All I know is that this came from a machine with a cryptic ID of just 'hello'.

So we then try to brute force the `UID`:

```python
import subprocess

BCV = "93iNKe0zcKfgfSwQoHYdJbWGu4Dfnw5ZZ5a3ld5UEqI="

for uid in range(0, 10000):
    cmd = f'echo "{BCV}" | openssl enc -d -aes-256-cbc -md sha256 -nosalt -k "B-hello-{uid}" -a -A'
    result = subprocess.run(cmd, shell=True, capture_output=True)
    if result.returncode == 0:
        print(f"UID {uid} succeeded: {result.stdout}")

# UID 83 succeeded: b'B\x87\xe5\xb5\xa5\x1d\xc9\`Ww+3\x8d\xb8\xa9\x06\x7f\x0f\x1dY\xa3\xe5\xf3\x080I&/\x98N\x01'
# UID 1094 succeeded: b'\x10CU1\\\xe3E\xbf\x9e\x83\xa7\xbb\xf6\xda\xc6\x90\xb3\x17O\x9e\xf5\x1c\xbe\x92\xad\xbd}\xd1\x82\x84H'
# UID 1338 succeeded: b'TEST-VALUE-VERIFY\n'
# UID 1417 succeeded: b'\xe0b[\xc2.\x08W\xb5\x15\xc9?\xf0an0W4I\xa3+\xdbb\x0f\xa8\n"\xd2\'\x85yj'
# ...
```

And get the first key: `"B-hello-1338"`.

`_bcl_get` function returns the second key `"hello-1338"` by `echo`, which is `_k` used in:

```sh
_k="$(_bcl_get)" && _P="$(echo "$1" | openssl enc -d -aes-256-cbc -md sha256 -nosalt -k "$_k" -a -A 2> /dev/null)";
```

```python
import subprocess

P = "llLvO8+J6gmLlp964bcJG3I3mY27I9ACsJTvXYCZv2Q="
_k = "hello-1338"  # from dec-1.py

cmd = f'echo "{P}" | openssl enc -d -aes-256-cbc -md sha256 -nosalt -k "{_k}" -a -A'
result = subprocess.run(cmd, shell=True, capture_output=True)

print(result.stdout)  # b'QHh4K9JfgoACd2f4\n'
```

Then we can get the string `"QHh4K9JfgoACd2f4"` by running the above command, which is `_P` used in the third key:

```sh
str="$(echo "$C" | openssl enc -d -aes-256-cbc -md sha256 -nosalt -k "C-${S}-${_P}" -a -A 2>/dev/null)"
```

Here `str` turns out to be `"R=2105\\n\\n"`.

## Flag

```
flag{f2ea4caf879bde891f0174f528c20682}
Congraulations!
```
