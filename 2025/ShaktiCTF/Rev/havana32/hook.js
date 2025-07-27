const base = Module.findBaseAddress("havana32.exe");

const fn_read = base.add(0x6A40); // read buffer
const var_buffer = base.add(0x474C0); // buffer
Interceptor.replace(fn_read, new NativeCallback(function (a1, a2, a3) {
    console.log("fn_read called, arg1=" + a1 + ", (buffer=" + var_buffer + ")");
    const input = "[INPUT]";
    Memory.writeAnsiString(var_buffer, input);
    console.log("Data written to var_buffer: " + var_buffer.readAnsiString(), input.length);
    return 1;
}, "int", ["pointer", "int", "int"]));

const fn_vm_main = base.add(0x1300);
const var_matched = base.add(0x474B8); // matched count
Interceptor.attach(fn_vm_main, {
    onLeave: function () {
        const matched = Memory.readU32(var_matched);
        console.log("matched:", matched);
        send({ matched: matched });
    }
});