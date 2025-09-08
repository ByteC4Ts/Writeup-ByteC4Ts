## Solution

We extracted the code that checks the flag from IDA, the code is composed of flattened switch-case statements.

```python
code = """
_BOOL8 __fastcall check_flag(__int64 a1)
{
  char v2; // [rsp+1Bh] [rbp-5h]
  int v3; // [rsp+1Ch] [rbp-4h]

  if ( strlen((const char *)a1) != 31 )
    return 0LL;
  v2 = 66;
  v3 = 9493;
  while ( v3 && v3 != -1 )
  {
    switch ( v3 )
    {
      case 65519:
        if ( (unsigned __int8)((v2 ^ *(_BYTE *)(a1 + 23)) + 47) == 195 )
        {
          v2 = (*(_BYTE *)(a1 + 23) ^ v2) + 47;
          v3 = 28243;
        }
        else
        {
          v3 = -1;
        }
        break;
      case 65040:
        if ( (unsigned __int8)((v2 ^ *(_BYTE *)(a1 + 30)) + 49) == 69 )
        {
          v2 = (*(_BYTE *)(a1 + 30) ^ v2) + 49;
          v3 = 17079;
        }
        else
        {
          v3 = -1;
        }
        break;
      case 64790:
        if ( ((unsigned __int8)(v2 + *(_BYTE *)(a1 + 28)) ^ 0xB5) == 224 )
        {
          v2 = (*(_BYTE *)(a1 + 28) + v2) ^ 0xB5;
          v3 = 65519;
        }
        else
        {
          v3 = -1;
        }
        break;
      case 64556:
        if ( ((unsigned __int8)(v2 + *(_BYTE *)(a1 + 2)) ^ 0x5B) == 21 )
        {
          v2 = (*(_BYTE *)(a1 + 2) + v2) ^ 0x5B;
          v3 = 54841;
        }
        else
        {
          v3 = -1;
        }
        break;

        ......
"""
```

As we can see, the code is highly structured, and we can extract the constants of each `case` block using regular expressions.

We manually made a few adjustments to make the regular expression simpler, for example, changing `*(_BYTE *)a1` to `*(_BYTE *)(a1 + 0)` to make the pattern more uniform.

The following is the solve script:

```python
import re

matches = re.findall(r"      (.*?)break;", code, re.DOTALL)
jmpmap = {}


def process_block(match):
    lines = match.strip().splitlines()
    idx = re.findall(r"case (\d+):", lines[0])[0]
    p1 = re.findall(r"\(v2 (.) \*\(_BYTE \*\)\(a1 \+ (\d+)\)\) (.) (.*?)\) == (\d+)", lines[1])[0]
    stmt = re.sub(r"\*\(_BYTE \*\)\(a1 \+ \d+\)", "FLAGCHAR", lines[3]).strip(" ;")
    p2 = re.findall(r"v3 = (\d+);", lines[4])[0]
    jmpmap[idx] = (p1, stmt, p2)


for match in matches:
    process_block(match)

v2 = 66
v3 = 9493
flag = ["."] * 31

cnt = 0
while "." in flag:
    p1, stmt, p2 = jmpmap[str(v3)]
    op1, offset, op2, val1, val2 = p1

    eval_stmt = val2
    if op2 == "+":
        eval_stmt += "-"
    elif op2 == "-":
        eval_stmt += "+"
    elif op2 == "^":
        eval_stmt += "^"
    eval_stmt += val1

    eval_stmt = "(" + eval_stmt + ")"

    if op1 == "+":
        eval_stmt = f"{eval_stmt}-v2"
    elif op1 == "-":
        eval_stmt = f"v2-{eval_stmt}"
    elif op1 == "^":
        eval_stmt = f"v2^{eval_stmt}"

    flagchar = eval(eval_stmt) % 256

    flag[int(offset)] = chr(flagchar)
    print(f"{cnt:3} flag[{int(offset):2}]={chr(flagchar)}", "".join(flag))
    cnt += 1

    v2 = eval(stmt[4:].replace("FLAGCHAR", str(flagchar))) & 0xFF
    v3 = int(p2)
```

We get flag after 121 iterations:

```
  0 flag[23]=t .......................t.......
  1 flag[ 0]=c c......................t.......
  2 flag[10]=4 c.........4............t.......
  3 flag[18]=1 c.........4.......1....t.......
  4 flag[26]=0 c.........4.......1....t..0....
  5 flag[20]=_ c.........4.......1._..t..0....
  6 flag[11]=t c.........4t......1._..t..0....
  7 flag[14]=r c.........4t..r...1._..t..0....
  8 flag[23]=t c.........4t..r...1._..t..0....
  9 flag[12]=3 c.........4t3.r...1._..t..0....
 10 flag[23]=t c.........4t3.r...1._..t..0....
 11 flag[23]=t c.........4t3.r...1._..t..0....
 12 flag[17]=_ c.........4t3.r.._1._..t..0....
 13 flag[28]=n c.........4t3.r.._1._..t..0.n..
 14 flag[ 4]=c c...c.....4t3.r.._1._..t..0.n..
 15 flag[10]=4 c...c.....4t3.r.._1._..t..0.n..
 16 flag[ 5]=o c...co....4t3.r.._1._..t..0.n..
 17 flag[23]=t c...co....4t3.r.._1._..t..0.n..
 18 flag[ 1]=r cr..co....4t3.r.._1._..t..0.n..
 19 flag[24]=_ cr..co....4t3.r.._1._..t_.0.n..
 20 flag[27]=u cr..co....4t3.r.._1._..t_.0un..
 21 flag[29]=d cr..co....4t3.r.._1._..t_.0und.
 22 flag[ 8]=f cr..co..f.4t3.r.._1._..t_.0und.
 23 flag[18]=1 cr..co..f.4t3.r.._1._..t_.0und.
 24 flag[ 9]=l cr..co..fl4t3.r.._1._..t_.0und.
 25 flag[28]=n cr..co..fl4t3.r.._1._..t_.0und.
 26 flag[ 0]=c cr..co..fl4t3.r.._1._..t_.0und.
 27 flag[15]=t cr..co..fl4t3.rt._1._..t_.0und.
 28 flag[16]=h cr..co..fl4t3.rth_1._..t_.0und.
 29 flag[ 0]=c cr..co..fl4t3.rth_1._..t_.0und.
 30 flag[30]=} cr..co..fl4t3.rth_1._..t_.0und}
 31 flag[20]=_ cr..co..fl4t3.rth_1._..t_.0und}
 32 flag[25]=r cr..co..fl4t3.rth_1._..t_r0und}
 33 flag[30]=} cr..co..fl4t3.rth_1._..t_r0und}
 34 flag[ 6]=n cr..con.fl4t3.rth_1._..t_r0und}
 35 flag[ 2]=a cra.con.fl4t3.rth_1._..t_r0und}
 36 flag[17]=_ cra.con.fl4t3.rth_1._..t_r0und}
 37 flag[29]=d cra.con.fl4t3.rth_1._..t_r0und}
 38 flag[30]=} cra.con.fl4t3.rth_1._..t_r0und}
 39 flag[17]=_ cra.con.fl4t3.rth_1._..t_r0und}
 40 flag[ 6]=n cra.con.fl4t3.rth_1._..t_r0und}
 41 flag[ 6]=n cra.con.fl4t3.rth_1._..t_r0und}
 42 flag[15]=t cra.con.fl4t3.rth_1._..t_r0und}
 43 flag[13]=4 cra.con.fl4t34rth_1._..t_r0und}
 44 flag[ 4]=c cra.con.fl4t34rth_1._..t_r0und}
 45 flag[ 1]=r cra.con.fl4t34rth_1._..t_r0und}
 46 flag[ 4]=c cra.con.fl4t34rth_1._..t_r0und}
 47 flag[16]=h cra.con.fl4t34rth_1._..t_r0und}
 48 flag[21]=n cra.con.fl4t34rth_1._n.t_r0und}
 49 flag[30]=} cra.con.fl4t34rth_1._n.t_r0und}
 50 flag[25]=r cra.con.fl4t34rth_1._n.t_r0und}
 51 flag[ 8]=f cra.con.fl4t34rth_1._n.t_r0und}
 52 flag[26]=0 cra.con.fl4t34rth_1._n.t_r0und}
 53 flag[18]=1 cra.con.fl4t34rth_1._n.t_r0und}
 54 flag[ 7]={ cra.con{fl4t34rth_1._n.t_r0und}
 55 flag[30]=} cra.con{fl4t34rth_1._n.t_r0und}
 56 flag[30]=} cra.con{fl4t34rth_1._n.t_r0und}
 57 flag[18]=1 cra.con{fl4t34rth_1._n.t_r0und}
 58 flag[14]=r cra.con{fl4t34rth_1._n.t_r0und}
 59 flag[ 5]=o cra.con{fl4t34rth_1._n.t_r0und}
 60 flag[ 9]=l cra.con{fl4t34rth_1._n.t_r0und}
 61 flag[15]=t cra.con{fl4t34rth_1._n.t_r0und}
 62 flag[11]=t cra.con{fl4t34rth_1._n.t_r0und}
 63 flag[ 5]=o cra.con{fl4t34rth_1._n.t_r0und}
 64 flag[14]=r cra.con{fl4t34rth_1._n.t_r0und}
 65 flag[18]=1 cra.con{fl4t34rth_1._n.t_r0und}
 66 flag[29]=d cra.con{fl4t34rth_1._n.t_r0und}
 67 flag[28]=n cra.con{fl4t34rth_1._n.t_r0und}
 68 flag[14]=r cra.con{fl4t34rth_1._n.t_r0und}
 69 flag[12]=3 cra.con{fl4t34rth_1._n.t_r0und}
 70 flag[25]=r cra.con{fl4t34rth_1._n.t_r0und}
 71 flag[ 1]=r cra.con{fl4t34rth_1._n.t_r0und}
 72 flag[ 2]=a cra.con{fl4t34rth_1._n.t_r0und}
 73 flag[ 8]=f cra.con{fl4t34rth_1._n.t_r0und}
 74 flag[ 8]=f cra.con{fl4t34rth_1._n.t_r0und}
 75 flag[ 8]=f cra.con{fl4t34rth_1._n.t_r0und}
 76 flag[ 1]=r cra.con{fl4t34rth_1._n.t_r0und}
 77 flag[ 8]=f cra.con{fl4t34rth_1._n.t_r0und}
 78 flag[ 1]=r cra.con{fl4t34rth_1._n.t_r0und}
 79 flag[29]=d cra.con{fl4t34rth_1._n.t_r0und}
 80 flag[15]=t cra.con{fl4t34rth_1._n.t_r0und}
 81 flag[ 7]={ cra.con{fl4t34rth_1._n.t_r0und}
 82 flag[29]=d cra.con{fl4t34rth_1._n.t_r0und}
 83 flag[23]=t cra.con{fl4t34rth_1._n.t_r0und}
 84 flag[26]=0 cra.con{fl4t34rth_1._n.t_r0und}
 85 flag[22]=0 cra.con{fl4t34rth_1._n0t_r0und}
 86 flag[15]=t cra.con{fl4t34rth_1._n0t_r0und}
 87 flag[27]=u cra.con{fl4t34rth_1._n0t_r0und}
 88 flag[ 1]=r cra.con{fl4t34rth_1._n0t_r0und}
 89 flag[ 1]=r cra.con{fl4t34rth_1._n0t_r0und}
 90 flag[30]=} cra.con{fl4t34rth_1._n0t_r0und}
 91 flag[23]=t cra.con{fl4t34rth_1._n0t_r0und}
 92 flag[ 2]=a cra.con{fl4t34rth_1._n0t_r0und}
 93 flag[ 6]=n cra.con{fl4t34rth_1._n0t_r0und}
 94 flag[16]=h cra.con{fl4t34rth_1._n0t_r0und}
 95 flag[10]=4 cra.con{fl4t34rth_1._n0t_r0und}
 96 flag[23]=t cra.con{fl4t34rth_1._n0t_r0und}
 97 flag[19]=s cra.con{fl4t34rth_1s_n0t_r0und}
 98 flag[23]=t cra.con{fl4t34rth_1s_n0t_r0und}
 99 flag[24]=_ cra.con{fl4t34rth_1s_n0t_r0und}
100 flag[ 8]=f cra.con{fl4t34rth_1s_n0t_r0und}
101 flag[16]=h cra.con{fl4t34rth_1s_n0t_r0und}
102 flag[22]=0 cra.con{fl4t34rth_1s_n0t_r0und}
103 flag[12]=3 cra.con{fl4t34rth_1s_n0t_r0und}
104 flag[13]=4 cra.con{fl4t34rth_1s_n0t_r0und}
105 flag[20]=_ cra.con{fl4t34rth_1s_n0t_r0und}
106 flag[14]=r cra.con{fl4t34rth_1s_n0t_r0und}
107 flag[27]=u cra.con{fl4t34rth_1s_n0t_r0und}
108 flag[29]=d cra.con{fl4t34rth_1s_n0t_r0und}
109 flag[ 8]=f cra.con{fl4t34rth_1s_n0t_r0und}
110 flag[24]=_ cra.con{fl4t34rth_1s_n0t_r0und}
111 flag[18]=1 cra.con{fl4t34rth_1s_n0t_r0und}
112 flag[28]=n cra.con{fl4t34rth_1s_n0t_r0und}
113 flag[20]=_ cra.con{fl4t34rth_1s_n0t_r0und}
114 flag[21]=n cra.con{fl4t34rth_1s_n0t_r0und}
115 flag[13]=4 cra.con{fl4t34rth_1s_n0t_r0und}
116 flag[10]=4 cra.con{fl4t34rth_1s_n0t_r0und}
117 flag[21]=n cra.con{fl4t34rth_1s_n0t_r0und}
118 flag[20]=_ cra.con{fl4t34rth_1s_n0t_r0und}
119 flag[21]=n cra.con{fl4t34rth_1s_n0t_r0und}
120 flag[ 3]=c craccon{fl4t34rth_1s_n0t_r0und}
```

## Flag

```
craccon{fl4t34rth_1s_n0t_r0und}
```
