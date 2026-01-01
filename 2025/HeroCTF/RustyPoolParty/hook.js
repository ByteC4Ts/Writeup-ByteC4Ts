const base = Module.findBaseAddress("rusty_pool_party.exe");


// dynamic WinAPI resolver
const ptr_50CA = base.add(0x50CA);

function findExportName(base_addr, addr) {
    const m = Process.findModuleByAddress(base_addr);
    if (m == null) return null;
    for (const e of Module.enumerateExports(m.name)) {
        if (e.address.equals(addr)) {
            return m.name + "!" + e.name;
        }
    }
    return null;
}

Interceptor.attach(ptr_50CA, {
    onEnter: function (args) {
        this.arg0 = args[0];
        this.arg1 = args[1];
        this.arg2 = args[2];
    },
    onLeave: function (retval) {
        return; // <- comment out to enable logging
        console.log(`ptr_50CA(${this.arg0}, ${this.arg1}, ${this.arg2}) => ${retval} (${findExportName(this.arg0, retval)})`);
        console.log("\tBacktrace:");
        for (const ptr_bt of Thread.backtrace(this.context)) {
            console.log("\t" + ptr_bt);
        }
    }
});


// decoder functions
const ptr_4CC1 = base.add(0x4CC1);
const ptr_4E41 = base.add(0x4E41);
const ptr_4DC1 = base.add(0x4DC1);
const ptr_4D41 = base.add(0x4D41);

function searchImm64(buffer) {
    // 48 B8~BF xx xx ... xx -> mov reg, imm64
    const bin = new Uint8Array(buffer);
    for (let i = 0; i < bin.length - 10; i++) {
        if (bin[i] === 0x48 && 0xB8 <= bin[i + 1] && bin[i + 1] <= 0xBF) {
            const imm64 = bin.slice(i + 2, i + 10);
            // const imm64_str = Array.from(imm64).map(b => 32 <= b && b < 127 ? String.fromCharCode(b) : '.').join('');
            if (!imm64.every(b => 0 <= b && b < 127)) continue;
            const imm64_str = Array.from(imm64).map(b => String.fromCharCode(b)).join('');
            const imm64_hex = Array.from(imm64).map(b => b.toString(16).padStart(2, '0')).join(' ');
            console.log(`${imm64_str} (${imm64_hex})\tat offset ${i}`);
        }
    }
}

for (const p of [ptr_4CC1, /*ptr_4E41,*/ ptr_4DC1, ptr_4D41]) {
    Interceptor.attach(p, {
        onEnter: function (args) {
            this.arg0 = args[0]; // ptr_out_struct
            this.arg1 = args[1]; // ptr_raw_data
        },
        onLeave: function (retval) {
            const size = Memory.readU64(this.arg0).toNumber();
            const addr = ptr(Memory.readU64(this.arg0.add(8)));
            const buffer = Memory.readByteArray(addr, size);
            console.log(`[*] decoder function ${p} returned, size=${size}, addr=${addr}`);
            searchImm64(buffer);
        }
    });
}


/*
In sub_1400014D9:
// ...
if (v9)
    sub_140001C8F(v4, v43);  <- call decoder: sub_140004CC1, 7392 Bytes
if (v19)
    sub_1400032E8(v15, v44); <- call decoder: sub_140004E41, 6384 Bytes
if (v22)
    sub_140002402(v5, v45);  <- call decoder: sub_140004D41, 7728 Bytes
if (v21)
    sub_140002B75(v6, v46);  <- call decoder: sub_140004DC1, 3200 Bytes


sub_1400032E8 is not called so we have to patch the logic...
.text:000000014000185B loc_14000185B:
.text:000000014000185B                 test    dil, dil               ; <- patch here
.text:000000014000185E                 jz      short loc_14000186F
.text:0000000140001860                 mov     ecx, esi
.text:0000000140001862                 mov     rdx, [rsp+298h+var_208]
.text:000000014000186A                 call    sub_1400032E8
*/
Interceptor.attach(base.add(0x185B), {
    onEnter(args) {
        this.context.rdi = 1;
    }
});
const ptr_32E8 = base.add(0x32E8);
Interceptor.attach(ptr_32E8, {
    onEnter(args) {
        console.log("[+] ptr_32E8 called");
        const ptr_raw_data = args[1]; // ptr_raw_data

        // call decoder manually
        const fn_4E41 = new NativeFunction(ptr_4E41, 'pointer', ['pointer', 'pointer']);
        const ptr_out_struct = Memory.alloc(16);
        fn_4E41(ptr_out_struct, ptr_raw_data);
        const size = Memory.readU64(ptr_out_struct).toNumber();
        const addr = ptr(Memory.readU64(ptr_out_struct.add(8)));
        const buffer = Memory.readByteArray(addr, size);
        console.log(`[+] manually called decoder function ${ptr_4E41} returned, size=${size}, addr=${addr}`);
        searchImm64(buffer);
    }
});

/*
> python loader.py
[*] decoder function 0x7ff7c97a4cc1 returned, size=7392, addr=0x18298bfcc20
T_2: t_K (54 5f 32 3a 20 74 5f 4b)      at offset 22
FLAG PAR (46 4c 41 47 20 50 41 52)      at offset 35
2: t_KiN (32 3a 20 74 5f 4b 69 4e)      at offset 53
d_0F_P0 (64 5f 30 46 5f 50 30 00)       at offset 71
[+] ptr_32E8 called
[+] manually called decoder function 0x7ff7c97a4e41 returned, size=6384, addr=0x18298bfcc20
FLAG PAR (46 4c 41 47 20 50 41 52)      at offset 0
T_1: YoU (54 5f 31 3a 20 59 6f 55)      at offset 12
1: YoU_l (31 3a 20 59 6f 55 5f 6c)      at offset 47
1K3_7h4 (31 4b 33 5f 37 68 34 00)       at offset 65
/res (2f 00 72 00 65 00 73 00)  at offset 1235
pons (70 00 6f 00 6e 00 73 00)  at offset 1265
/res (2f 00 72 00 65 00 73 00)  at offset 1455
pons (70 00 6f 00 6e 00 73 00)  at offset 1468
[*] decoder function 0x7ff7c97a4d41 returned, size=7728, addr=0x18298bff330
FLAG PAR (46 4c 41 47 20 50 41 52)      at offset 0
T_3: oL_ (54 5f 33 3a 20 6f 4c 5f)      at offset 12
_P4r7Y} (5f 50 34 72 37 59 7d 00)       at offset 47
[*] decoder function 0x7ff7c97a4dc1 returned, size=3200, addr=0x18298bfe520
FLAG PAR (46 4c 41 47 20 50 41 52)      at offset 0
T_0: Her (54 5f 30 3a 20 48 65 72)      at offset 12
: Hero{y (3a 20 48 65 72 6f 7b 79)      at offset 40
0u_700_ (30 75 5f 37 30 30 5f 00)       at offset 55
*/

// Hero{y0u_700_YoU_l1K3_7h4t_KiNd_0F_P0oL_P4r7Y}