from concurrent.futures import ThreadPoolExecutor
from challengeio import send
import json

args = [chr(i) for i in range(0, 256)]

with ThreadPoolExecutor(max_workers=50) as executor:
    results_map = executor.map(send, args)

results = list(results_map)

with open("findcmds.json", "r") as f:
    cmds = json.load(f)

for i, result in enumerate(results):
    i = str(i)
    if result == "" or result == "timeout":
        continue
    elif i not in cmds or cmds[i] == "" or cmds[i] == "timeout":
        cmds[i] = result
    elif cmds[i] != result:
        cmds[i] = result
        print(f'Conflict for {i}: "{cmds[i]}" & "{result}"')

with open("findcmds.json", "w") as f:
    json.dump(cmds, f, indent=4)
