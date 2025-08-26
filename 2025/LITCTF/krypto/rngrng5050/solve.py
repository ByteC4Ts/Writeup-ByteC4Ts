from Crypto.Util.number import long_to_bytes as ltb
import os

dir = os.path.dirname(__file__)


with open(dir + '/output.txt', 'r') as file:
    data = file.read().strip().split('\n')[:-1]


predict = ''

for i in range(256):
    count = sum(int(elm[i], 2) for elm in data)
    print(count)
    predict += '1' if count < 500 else '0'


print(ltb(int(predict, 2)))

