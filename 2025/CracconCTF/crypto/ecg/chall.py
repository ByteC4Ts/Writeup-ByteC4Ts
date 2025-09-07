from Crypto.Util.number import *
import random, string

random.seed(1337)
red = ''.join(random.choices(string.ascii_letters, k=16)) #fake stuff

flag = f'craccon{{{red}}}'.encode()
message = flag[8:-1]
blocks = []

for i in range(len(message)//4):
  blocks.append(message[i*4:i*4+4])

n = bytes_to_long(blocks[0])
s0 =  bytes_to_long(blocks[1])
c = bytes_to_long(blocks[2])
m = bytes_to_long(blocks[3])

assert len(blocks)==4 

e = 2**65537
s=[]
s.append((s0*pow(m,e,n)+c)%n)
for i in range(10):
  s.append((s[-1]*pow(m,e,n)+c)%n)


print(s)
"[1471188920,8580498,528503476,577384753,534687615,631132756,1181691587,494356384,450508778,224733577,240456085]"
