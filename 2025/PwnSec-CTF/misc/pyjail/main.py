#!/usr/bin/python3

SAFE_BUILTINS = {
    "next": next,
    "open": open,
}

ALLOWED_CHARS = "abcefghijklmnopqrstuvwxyz()."


def is_unsafe(i: str) -> bool:
    return any(c not in ALLOWED_CHARS for c in i) or len(i) > 64 or 'str' in i or i.count('.') > 1


def main():
    user_input = input("Input: ")
    if is_unsafe(user_input):
        print("Nope!!")
        exit()

    print(eval(user_input, {"__builtins__": SAFE_BUILTINS}, {}))


if __name__ == "__main__":
    main()
