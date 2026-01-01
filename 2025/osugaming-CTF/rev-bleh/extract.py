import os
import json


def extract(path):
    with open(path, "rb") as f:
        data = f.read()
    s = data[5562:5570] + data[5572:5580] + data[5590:5598] + data[5600:5608]
    return s.hex()


result = {}
root = "..."
for file in os.listdir(root):
    h = extract(os.path.join(root, file))
    result[file] = h

with open("extracted.json", "w") as f:
    json.dump(result, f, indent=4)
