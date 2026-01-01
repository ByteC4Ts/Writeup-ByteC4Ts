import frida

device = frida.get_usb_device()
pid = device.spawn(["com.heroctf.freeda3"])
session = device.attach(pid)


def on_message(message, data):
    if message["type"] == "error":
        line, col = message["lineNumber"], message["columnNumber"]
        filename = message["fileName"]
        stack = message["stack"]
        print(f"[!] {filename}, {line}:{col}\nStack:\n{stack}")


script_code = open("hook.js").read()
script = session.create_script(script_code)
script.on("message", on_message)
script.load()

device.resume(pid)

input()
