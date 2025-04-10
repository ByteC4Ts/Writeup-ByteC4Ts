import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
file = open("output.txt", "r").read().strip()


def reverse(str):
    return str[2] + str[0] + str[1]


def main():
    res = ""
    for i in range(0, 33, 3):
        res += reverse(file[i : i + 3])
    print(res[::-1])


if __name__ == "__main__":
    main()
