import frida
import time

pid = frida.spawn(["rusty_pool_party.exe"])
session = frida.attach(pid)


def on_message(message, data):
    if message["type"] == "error":
        line, col = message["lineNumber"], message["columnNumber"]
        filename = message["fileName"]
        stack = message["stack"]
        print(f"[!] {filename}, {line}:{col}\nStack:\n{stack}")


script_code = open("hook.js", "r", encoding="utf-8").read()
script = session.create_script(script_code)
script.on("message", on_message)
script.load()
frida.resume(pid)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    session.detach()
