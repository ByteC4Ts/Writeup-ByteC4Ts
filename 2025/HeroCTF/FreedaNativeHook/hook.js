Interceptor.attach(Module.getExportByName(null, "android_dlopen_ext"), {
    onEnter(args) {
        this.path = args[0].readCString();
        console.log("android_dlopen_ext:", this.path);
    },
    onLeave(retval) {
        if (this.path.includes("libv3.so")) {
            let base = Module.findBaseAddress("libv3.so");
            console.log("[*] libv3.so loaded at:", base);
            let ptr_get_flag = base.add(0x2810);
            Interceptor.attach(ptr_get_flag, {
                onEnter(args) {
                    console.log("[native] get_flag called");
                },
                onLeave(retval) {
                    let flag = retval.readCString();
                    console.log("[native] get_flag returned:", flag);
                    // [native] get_flag returned: Hero{F1NAL_57EP_Y0U_KN0W_H0W_TO_R3V3R53_4NDR01D}
                }
            });
        }
    }
});

Java.perform(function () {
    let CheckFlag = Java.use("com.heroctf.freeda3.utils.CheckFlag");
    CheckFlag["checkFlag"].implementation = function (input) {
        console.log(`CheckFlag.checkFlag is called: input=${input}`);
        return this["checkFlag"](input);
    };
})

// Hero{F1NAL_57EP_Y0U_KN0W_H0W_TO_R3V3R53_4NDR01D}