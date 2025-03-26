#include <iostream>
using namespace std;

string realflag(27, '\0');

int check(string flag) // it means recover now ;)
{
	// if(flag.length() != 27) return 1;

	unsigned char v[32] = {
        0xE1, 0xA7, 0x1E, 0xF8, 0x75, 0x23, 0x7B, 0x61,
        0xB9, 0x9D, 0xFC, 0x5A, 0x5B, 0xDF, 0x69,
		0xD2, 0xFE, 0x1B, 0xED, 0xF4, 0xED, 0x67, 0xF4,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
    };
	int charindex = 0, bitindex = 0;

	for(int i = 0; i <= 0x16; ++i)
	{
		for(int j = 0; j <= 7; ++j)
		{
			if(!bitindex) bitindex = 1;
			int bitmask1 = 1 << (7 - j);
			int bitmask2 = 1 << (7 - bitindex);

			// To better understand the process of comparison:
			// printf("checking i=%d, bitmask1=%d, charindex=%d, bitmask2=%d\n",
			//     i, bitmask1, charindex, bitmask2);

			// if( (bitmask1&v[i]) > 0 != (bitmask2&flag[charindex]) > 0 ) return 1;
			// Recover the original flag:
			if( (bitmask1&v[i]) > 0) realflag[charindex] |= bitmask2;

			if(++bitindex == 8)
			{
				bitindex = 0;
				++charindex;
			}

			if(charindex == 27) return 0;
		}
	}
	return 0;
}

int main()
{
	check(""); // anything
	cout << realflag << endl; // picoCTF{0n3_bi7_4t_a_7im3}
	return 0;
}