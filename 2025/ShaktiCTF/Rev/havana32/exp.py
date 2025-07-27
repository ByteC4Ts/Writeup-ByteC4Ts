import frida
import time


def pad49(password):
    return (password + "." * 100)[:49]


def try_password(password, expected_matched):
    pid = frida.spawn(["havana32.exe"])
    session = frida.attach(pid)
    script_code = open("hook.js", "r").read()
    script_code = script_code.replace("[INPUT]", pad49(password))
    script = session.create_script(script_code)
    ok = False

    def on_message(message, data):
        nonlocal ok
        if message["type"] == "send":
            matched = message["payload"]["matched"]
            if matched == expected_matched:
                ok = True

    script.on("message", on_message)
    script.load()
    frida.resume(pid)
    time.sleep(0.2)
    session.detach()
    return ok


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_{}"
flag = "shaktictf{"
while not flag.endswith("}"):
    for ch in alphabet:
        ok = try_password(flag + ch, len(flag) + 1)
        if ok:
            flag += ch
            print(f"[*] Current flag: {flag}")
            break

# shaktictf{H4lf_0f_mY_H34rt_1s_1n_H4v4n4_0oH_n4n4}

# note: not working on my ARM windows :(
