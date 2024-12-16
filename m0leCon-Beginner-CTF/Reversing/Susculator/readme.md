# m0leCon Beginner CTF

## Susculator

> ...

## Approach

Bruteforce.

```cpp
#include <iostream>
#define HIWORD(x) (((x) >> 16) & 0xFFFF)
using namespace std;
typedef unsigned int i32;
i32 myhash(i32 a1)
{
	i32 v2 = -793289518 * ((-793289518 * (a1 ^ HIWORD(a1))) ^ ((-793289518 * (a1 ^ HIWORD(a1))) >> 16));
	return HIWORD(v2) ^ v2;
}
int main()
{
	int target=-1554755408;
	for(i32 test=0;;test++)
	{
		if(test%100000000==0) cout<<test<<endl;
		if(target==myhash(test))
		{
			cout<<test<<endl; // 733394619
			break;
		}
	}
	cout<<"Done.";
	return 0;
}
```

## Flag

```
ptm{my_s3cr3t_i5_th4t_1_l0v3_c4t5}
```
