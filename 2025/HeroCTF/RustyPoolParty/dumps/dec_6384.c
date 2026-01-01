int64_t sub_0()
{
    int64_t var_10a;
    __builtin_strcpy(&var_10a, "FLAG PART_1: YoU_l1K3_7h4");

    if (var_10a == 0x58)
        return 0;

    void var_d0;
    int64_t rdi_1 = __builtin_memset(&var_d0, 0, 0x88);

    if (sub_970(&var_d0))
        return 1;

    void* var_a0;
    void* rax_3 = sub_f70(var_a0, 0xa215c401);
    void* rax_4 = sub_f70(var_a0, 0x58d5d3e6);
    void* rax_5 = sub_f70(var_a0, 0x8a851d20);
    void* rax_6 = sub_f70(var_a0, 0x54fcc943);
    void* rax_7 = sub_f70(var_a0, 0x7f07c44a);
    void* rax_8 = sub_f70(var_a0, 0xfaba0065);
    sub_f70(var_a0, 0xe53f7a31);
    void* rax_9 = sub_f70(var_a0, 0xafd195a6);
    int64_t rax_11;
    int64_t rdx;
    int64_t rsi_1;
    int64_t rdi_2;
    int64_t r8;
    rax_11 = sub_f70(var_a0, 0xf9d2dde2)(rdi_1, rax_3, 1, 0, 0, 0);

    if (!rax_11)
    {
        sub_6a0(rdi_2, rsi_1, rdx, &var_d0, r8);
        void* rax_12 = sub_1020(0xa3e6f6c3);

        if (rax_12)
        {
            void* rax_13 = sub_f70(rax_12, 0xf9d2dde2);
            void* rax_14 = sub_f70(rax_12, 0x71948ca4);

            if (rax_13 && rax_14 && rax_13())
                rax_14();
        }

        while (true)
            /* nop */

        return;
    }

    int64_t var_124 = 0x1a217b644e9c90f6;
    *(&var_124 + 5) = -0x7745d5069de5de85;
    void var_117;
    sub_8f0(&var_124, &var_117);
    int64_t var_180 = 0;
    int32_t var_188 = 0;
    int32_t var_190 = 0x2000;
    int32_t var_198 = 0x2000;

    if (rsi_1() == -1)
    {
        int64_t rdx_2;
        int64_t rsi_3;
        int64_t rdi_3;
        int64_t r8_1;
        rdx_2 = rax_8();
        sub_6a0(rdi_3, rsi_3, rdx_2, &var_d0, r8_1);
        void* rax_17 = sub_1020(0xa3e6f6c3);

        if (rax_17)
        {
            void* rax_18 = sub_f70(rax_17, 0xf9d2dde2);
            void* rax_19 = sub_f70(rax_17, 0x71948ca4);

            if (rax_18 && rax_19 && rax_18())
                rax_19();
        }

        while (true)
            /* nop */

        return;
    }

    void var_f0;
    void* var_168 = &var_f0;

    while (true)
    {
        int64_t var_d8_1 = rax_11;
        __builtin_memset(&var_f0, 0, 0x18);
        rax_4(0);
        int32_t rdi_5 = sub_18a0(&var_d0, rax_11);
        var_198 = 0;
        int64_t rsi_6;
        int64_t rdi_6;
        rsi_6 = rax_6();
        char var_142;

        if (rdi_5 != 5)
            rax_9();
        else if (var_142 == 7)
        {
            rax_9();
            rax_5();
            rax_8();
            int64_t rdx_6;
            int64_t rsi_7;
            int64_t rdi_7;
            int64_t r8_2;
            rdx_6 = rax_8();
            sub_6a0(rdi_7, rsi_7, rdx_6, &var_d0, r8_2);
            void* rax_25 = sub_1020(0xa3e6f6c3);

            if (rax_25)
            {
                void* rax_29 = sub_f70(rax_25, 0xf9d2dde2);
                void* rax_30 = sub_f70(rax_25, 0x71948ca4);

                if (rax_29 && rax_30 && rax_29())
                    rax_30();
            }

            while (true)
                /* nop */
        }
        else
        {
            int64_t var_138;
            int64_t var_130;

            if (var_142 != 2)
            {
                int32_t var_141;

                if (var_142 == 6)
                {
                    int64_t var_c8;

                    if (!var_141)
                    {
                        int64_t rax_28;
                        int64_t rdi_12;
                        rax_28 = sub_1350(var_c8, rsi_6, 0x40, &var_d0);
                        var_c8 = rax_28;

                        if (rax_28)
                        {
                            __builtin_memcpy(rax_28, "/response", 0x14);
                            var_138 = 0;
                            var_130 = 0;
                            var_190 = &var_130;
                            var_198 = &var_138;
                            sub_13e0(0, &var_d0, sub_0, sub_0);
                            int64_t rdx_13 = var_138;

                            if (rdx_13)
                                rsi_6 = sub_13b0(rdi_12, rsi_6, rdx_13, &var_d0);

                            var_c8 = sub_13b0(rdi_12, rsi_6, var_c8, &var_d0);
                        }
                    }
                    else
                    {
                        int64_t rax_26 = sub_1350(rdi_6, rsi_6, var_141, &var_d0);

                        if (rax_26)
                        {
                            var_198 = 0;
                            int64_t rsi_8;
                            int64_t rdi_9;
                            rsi_8 = rax_6(rax_26);
                            int64_t r15_1 = var_c8;
                            int64_t rax_27;
                            int64_t rsi_9;
                            int64_t* rdi_10;
                            rax_27 = sub_1350(rdi_9, rsi_8, 0x40, &var_d0);
                            var_c8 = rax_27;

                            if (rax_27)
                            {
                                __builtin_memcpy(rax_27, "/response", 0x14);
                                var_190 = &var_130;
                                var_198 = &var_138;
                                var_138 = 0;
                                var_130 = 0;
                                sub_13e0(0, &var_d0, rdi_10, var_141);
                                int64_t rdx_9 = var_138;

                                if (rdx_9)
                                    rsi_9 = sub_13b0(rdi_10, rsi_9, rdx_9, &var_d0);

                                rsi_9 = sub_13b0(rdi_10, rsi_9, var_c8, &var_d0);
                                var_c8 = r15_1;
                            }

                            sub_13b0(rdi_10, rsi_9, rdi_10, &var_d0);
                        }
                    }
                }
                rax_9();
            }
            else
            {
                var_138 = 0;
                var_190 = &var_130;
                var_198 = &var_138;
                var_130 = 0;

                if (sub_13e0(1, &var_d0, sub_0, sub_0) || !var_138)
                    rax_9();
                else
                {
                    int64_t rax_23 = var_130;

                    if (!rax_23)
                        rax_9();
                    else
                    {
                        int32_t var_148 = 0;
                        var_198 = 0;
                        char var_13d = 3;
                        int32_t var_13c_1 = rax_23;
                        rax_7();
                        var_198 = 0;
                        rax_7();
                        int64_t rsi_5;
                        int64_t rdi_4;
                        rsi_5 = rax_9();
                        sub_13b0(rdi_4, rsi_5, var_138, &var_d0);
                    }
                }
            }
        }
        rax_5();
        sub_f70(var_a0, 0x68fe748)();
    }
}

void sub_6a0(int64_t arg1, int64_t arg2, int64_t arg3, int64_t* arg4, int64_t arg5)
{
    int64_t rdx = *arg4;
    int64_t rax;

    if (rdx)
    {
        rax = sub_13b0(arg1, arg2, rdx, arg4);
        arg5 = 0;
        *arg4 = 0;
    }

    int64_t rdx_1 = arg4[1];

    if (rdx_1)
    {
        rax = sub_13b0(arg1, arg2, rdx_1, arg4, arg5);
        arg4[1] = 0;
    }

    int64_t rdx_2 = arg4[2];

    if (rdx_2)
    {
        rax = sub_13b0(arg1, arg2, rdx_2, arg4);
        arg4[2] = 0;
    }

    int64_t rdx_3 = arg4[3];

    if (rdx_3)
    {
        sub_13b0(arg1, arg2, rdx_3, arg4);
        arg4[3] = 0;
    }
}

void* __convention("win64") sub_710(int64_t arg1, void* arg2)
{
    void* rax = sub_f70(arg2, 0xbdcac9ce);
    void* rax_1 = sub_f70(arg2, 0x7f07c44a);
    void* rax_2 = sub_f70(arg2, 0xfaba0065);
    void* r12 = sub_f70(arg2, 0xb7f5e1c2);
    void* result;
    result = !rax;
    result |= !rax_1;

    if (!result && rax_2)
    {
        int64_t var_80;
        __builtin_memcpy(&var_80,
            "\xaa\xcc\xb2\x12\x14\x12\x51\x7f\x3e\x9a\x45\xd7\x88\x1b\xf3\x26\xe9\xf6\xee\x47\x67\x77\x"
        "23\x0c\x62\xe8\x2a\xb8\xfc\x47\x90\x49\xc7\x93\xd6\x77\x76\x67\x36\x51\x4a\xe2\x31\x
                d7",
            0x2c);
        char var_54[0x24];

        for (int64_t i = 0; i != 0x1c; i += 1)
        {
            uint64_t rdx_2;
            rdx_2 = *(&var_80 + (i & 0xf));
            int64_t var_70;
            rdx_2 ^= *(&var_70 + i);
            var_54[i] = rdx_2;
        }

        int32_t var_a0_1 = 0x80;
        int64_t var_98_1 = 0;
        int32_t var_a8_1 = 4;
        int64_t rsi_1;
        int64_t rdi_1;
        result = rax(rax_1, arg1, 0x40000000, &var_54, 1, 0);

        if (result != -1)
        {
            if (r12)
                rsi_1 = r12();

            int32_t r8_1 = 0;
            var_80 = 0;

            while (*(rsi_1 + r8_1))
                r8_1 += 1;

            var_a8_1 = 0;
            var_a8_1 = 0;
            rdi_1()();
            return rax_2();
        }
    }

    return result;
}

int64_t __convention("win64") sub_8b0(char* arg1, char* arg2)
{
    int64_t i = 0;
    int64_t var_18 = 0x7f51121412b2ccaa;
    int64_t var_10 = 0x26f31b88d7459a3e;

    do
    {
        arg2[i] = arg1[i] ^ *(&var_18 + i);
        i += 1;
    } while (i != 0xc);

    return i;
}

int64_t __convention("win64") sub_8f0(char* arg1, char* arg2)
{
    int64_t i = 0;
    int64_t var_18 = 0x7f51121412b2ccaa;
    int64_t var_10 = 0x26f31b88d7459a3e;

    do
    {
        arg2[i] = arg1[i] ^ *(&var_18 + i);
        i += 1;
    } while (i != 0xd);

    return i;
}

int64_t __convention("win64") sub_930(char* arg1, char* arg2)
{
    int64_t i = 0;
    int64_t var_18 = 0x7f51121412b2ccaa;
    int64_t var_10 = 0x26f31b88d7459a3e;

    do
    {
        arg2[i] = arg1[i] ^ *(&var_18 + i);
        i += 1;
    } while (i != 0xa);

    return i;
}

int64_t __convention("win64") sub_970(int64_t* arg1)
{
    arg1[6] = sub_1020(0xa3e6f6c3);
    int64_t rax_1 = sub_1020(0xa62a3b3b);
    void* rcx = arg1[6];
    arg1[5] = rax_1;

    if (rax_1 && rcx)
    {
        void* rax_2 = sub_f70(rcx, 0x86fe8652);
        void* rcx_1 = arg1[5];
        arg1[0xd] = rax_2;
        void* rax_3 = sub_f70(rcx_1, 0xb3f819f8);
        void* rcx_2 = arg1[6];
        arg1[0xe] = rax_3;
        void* rax_4 = sub_f70(rcx_2, 0x29630f3d);
        void* rcx_3 = arg1[5];
        arg1[0xf] = rax_4;
        void* rax_5 = sub_f70(rcx_3, 0xa05ab779);
        arg1[0x10] = rax_5;

        if (arg1[0xd] && arg1[0xe] && arg1[0xf] && rax_5)
        {
            void* rax_6 = sub_f70(arg1[6], 0x53b2070f);

            if (rax_6)
            {
                int64_t var_156 = 0x1b7f202760d7bfdf;
                *(&var_156 + 7) = 0x45f6521b;
                int64_t var_5a_1 = 0x26f31b88d7459a3e;
                int64_t var_62 = 0x7f51121412b2ccaa;

                for (int64_t i = 0; i != 0xb; )
                {
                    char var_14b[0xb];
                    var_14b[i] = *(&var_156 + i) ^ *(i + &var_62);
                    i += 1;
                    char (* var_198_1)[0xb] = &var_14b;
                }

                int32_t var_138_1 = 0xd729f65a;
                void var_134;
                void* var_1a0_1 = &var_134;
                int64_t var_140 = 0x512166607adca5dd;
                sub_8b0(&var_140, &var_134);
                int64_t var_110 = 0x4d627b6473c4a8cb;
                *(&var_110 + 5) = -0x7744d601efb29d85;
                void var_103;
                sub_8f0(&var_110, &var_103);
                int64_t var_128 = 0x516321787ed7a4d9;
                int32_t var_120_1 = 0xd729f65a;
                void var_11c;
                sub_8b0(&var_128, &var_11c);
                int64_t var_17e = 0x13353c2621dba8cd;
                int16_t var_176_1 = 0x9a52;
                void var_174;
                sub_930(&var_17e, &var_174);
                int64_t var_16a = 0x13353c797fdca5dd;
                int16_t var_162_1 = 0x9a52;
                void var_160;
                sub_930(&var_16a, &var_160);
                int64_t rax_7;
                int64_t rdi_2;
                rax_7 = rax_6();
                arg1[7] = rax_7;
                int64_t rax_8;
                int64_t rdi_3;
                rax_8 = rdi_2();
                arg1[8] = rax_8;
                int64_t rax_9;
                int64_t rdi_4;
                rax_9 = rdi_3();
                arg1[9] = rax_9;
                int64_t rax_10;
                int64_t rdi_5;
                rax_10 = rdi_4();
                arg1[0xa] = rax_10;
                int64_t rax_11;
                int64_t rdi_6;
                rax_11 = rdi_5();
                arg1[0xb] = rax_11;
                int64_t rax_12;
                int64_t rsi_1;
                int64_t rdi_7;
                rax_12 = rdi_6();
                arg1[0xc] = rax_12;
                int64_t rax_13;
                int64_t rsi_2;
                int64_t rdi_8;
                rax_13 = sub_1350(rdi_7, rsi_1, 0x200, arg1);
                *arg1 = rax_13;
                int64_t rax_14;
                int64_t rsi_3;
                int64_t rdi_9;
                rax_14 = sub_1350(rdi_8, rsi_2, 0x100, arg1);
                arg1[1] = rax_14;
                int64_t rax_15;
                int64_t rsi_4;
                int64_t rdi_10;
                rax_15 = sub_1350(rdi_9, rsi_3, 0x50, arg1);
                arg1[2] = rax_15;
                int64_t rax_16;
                int16_t* rsi_5;
                rax_16 = sub_1350(rdi_10, rsi_4, 0x80, arg1);
                arg1[3] = rax_16;
                int16_t* rax_17 = *arg1;

                if (rax_17)
                {
                    int128_t* rcx_14 = arg1[1];

                    if (rcx_14)
                    {
                        int128_t* rdi_11 = arg1[2];

                        if (rdi_11 && rax_16)
                        {
                            int64_t i_1 = 0;
                            int64_t var_b0;
                            __builtin_memcpy(&var_b0,
                                "\xce\xb5\xdc\x23\x26\x3c\x39\x1a\x4c\xf5\x26\xa3\xee\x35\x95\x54\xaa",
                                0x11);
                            var_62 = 0x7f51121412b2ccaa;
                            int64_t var_5a_2 = 0x26f31b88d7459a3e;
                            char var_9f[0x11];
                            uint64_t r8_2;

                            do
                            {
                                r8_2 = *(&var_62 + (i_1 & 0xf));
                                r8_2 ^= *(&var_b0 + i_1);
                                var_9f[i_1] = r8_2;
                                i_1 += 1;
                            } while (i_1 != 0x11);

                            int64_t i_2;

                            for (i_2 = 0; i_2 != 0x11; i_2 += 1)
                            {
                                r8_2 = var_9f[i_2];
                                rsi_5[i_2] = r8_2;
                            }

                            while (true)
                            {
                                i_2 = *rsi_5;

                                if (!i_2)
                                    break;

                                *rax_17 = i_2;
                                rsi_5 = &rsi_5[1];
                                rax_17 = &rax_17[1];
                            }

                            *rax_17 = 0;
                            char var_188_1 = 0x3e;
                            int64_t var_74_1 = 0x26f31b88d7459a3e;
                            int64_t var_190 = 0x1b3f73797fddaf85;
                            int64_t var_7c = 0x7f51121412b2ccaa;
                            char var_187[0x9];

                            for (int64_t i_3 = 0; i_3 != 9; i_3 += 1)
                            {
                                int16_t rdx_8;
                                rdx_8 = *(&var_190 + i_3);
                                rdx_8 ^= *(i_3 + &var_7c);
                                var_187[i_3] = rdx_8;
                            }

                            int128_t var_8e;
                            int64_t i_4;

                            for (i_4 = 0; i_4 != 9; i_4 += 1)
                                *(&var_8e + (i_4 << 1)) = var_187[i_4];

                            int16_t var_7e;
                            i_4 = var_7e;
                            int128_t zmm0_1 = var_8e;
                            rcx_14[1] = i_4;
                            int64_t var_f6 = 0xb3f777353f498e9;
                            *rcx_14 = zmm0_1;
                            *(&var_f6 + 5) = -0x77189454eef4c089;
                            char var_e9[0xd];
                            sub_8f0(&var_f6, &var_e9);

                            for (int64_t i_5 = 0; i_5 != 0xd; i_5 += 1)
                            {
                                char (* rdx_9)[0xd];
                                rdx_9 = var_e9[i_5];
                                *(&var_7c + (i_5 << 1)) = rdx_9;
                            }

                            int128_t zmm1_1 = var_7c;
                            int64_t var_dc = 0x1b3e71787ed7a4d9;
                            int64_t var_b8_1 = 0x26f31b88d7459a3e;
                            *(&var_dc + 6) = 0x1be6be27b45b1b3e;
                            int64_t var_c0 = 0x7f51121412b2ccaa;
                            int64_t i_6 = 0;
                            *rdi_11 = zmm1_1;
                            *(rdi_11 + 0xa) = *(&var_74_1 + 2);
                            char var_ce[0xe];

                            do
                            {
                                var_ce[i_6] = *(&var_dc + i_6) ^ *(&var_c0 + i_6);
                                i_6 += 1;
                            } while (i_6 != 0xe);

                            for (int64_t i_7 = 0; i_7 != 0xe; i_7 += 1)
                            {
                                int64_t* rcx_15;
                                rcx_15 = var_ce[i_7];
                                arg1[3][i_7] = rcx_15;
                            }

                            *(arg1 + 0x24) = 0x2f9a;
                            arg1[4] = 0x3e8;
                            return 0;
                        }
                    }
                }
            }
        }
    }

    return 1;
}

int64_t sub_e90()
{
    void* gsbase;
    return *(gsbase + 0x30);
}

void* sub_ea0()
{
    void* gsbase;
    void* result = *(gsbase + 0x30);

    if (!result)
        return result;

    return *(result + 0x60);
}

int64_t __convention("win64") sub_ec0(int64_t arg1, int64_t arg2, char* arg3)
{
    int64_t i;

    for (i = 0; i != arg2; i += 1)
    {
        int32_t r9;
        r9 = *(arg1 + (i << 1));

        if (r9 - 0x41 <= 0x19)
            r9 += 0x20;

        arg3[i] = r9;
    }

    return i;
}

uint64_t __convention("win64") sub_ef0(char* arg1, int32_t arg2)
{
    int64_t i = 0;
    int32_t rax = -1;

    for (; i < arg2; i += 1)
    {
        int32_t r11;
        r11 = arg1[i];
        int64_t j_1 = 8;
        int64_t j;

        do
        {
            int32_t r8_2 = rax ^ r11;
            r11 s>>= 1;
            rax = rax >> 1 ^ (-((r8_2 & 1)) & 0xedb88320);
            j = j_1;
            j_1 -= 1;
        } while (j != 1);
    }

    return ~rax;
}

int64_t __convention("win64") sub_f40(char* arg1, int32_t arg2)
{
    int32_t result = -0x7ee3623b;

    while (arg1 < &arg1[arg2])
    {
        uint32_t r8_1 = *arg1;
        arg1 = &arg1[1];
        result = (result ^ r8_1) * 0x1000193;
    }

    return result;
}

void* __convention("win64") sub_f70(void* arg1, int32_t arg2)
{
    if (!arg1)
        return 0;

    int32_t* rax_1 = *(arg1 + 0x3c) + arg1;

    if (*rax_1 == 0x4550)
    {
        int64_t i = 0;
        void* rsi_2 = rax_1[0x22] + arg1;
        uint64_t rdi_1 = *(rsi_2 + 0x1c);
        uint64_t rbp_1 = *(rsi_2 + 0x24);
        int32_t* r12_2 = *(rsi_2 + 0x20) + arg1;

        for (; i < *(rsi_2 + 0x14); i += 1)
        {
            uint64_t r14_1 = *r12_2;

            if (sub_f40(r14_1 + arg1, sub_10f0(r14_1 + arg1)) == arg2)
                return *(rdi_1 + arg1 + (*(rbp_1 + arg1 + (i << 1)) << 2)) + arg1;

            r12_2 = &r12_2[1];
        }
    }

    return sub_0;
}

int64_t __convention("win64") sub_1020(int32_t arg1)
{
    char var_428[0x400];
    __builtin_memset(&var_428, 0, 0x400);
    void* rax = sub_ea0();

    if (rax)
    {
        void* rax_1 = *(rax + 0x18);

        if (rax_1)
        {
            void** rbx_1 = *(rax_1 + 0x20);

            for (int32_t i = 0; i != 0x64; i += 1)
            {
                if (rbx_1 == rax_1 + 0x20)
                    break;

                int64_t rcx = rbx_1[0xa];

                if (rcx)
                {
                    int16_t r11_1 = rbx_1[9];

                    if (r11_1)
                    {
                        r11_1 u>>= 1;
                        uint64_t rdx_1 = r11_1;

                        if (rdx_1 - 1 <= 0x3fe)
                        {
                            sub_ec0(rcx, rdx_1, &var_428);

                            if (sub_f40(&var_428, r11_1) == arg1)
                            {
                                int64_t result = rbx_1[4];
                                sub_12d0(&var_428, 0x400);
                                return result;
                            }

                            sub_12d0(&var_428, 0x400);
                        }
                    }
                }

                rbx_1 = *rbx_1;
            }
        }
    }

    return 0;
}

void* __convention("win64") sub_10f0(char* arg1)
{
    char* rax = arg1;

    while (*rax)
        rax = &rax[1];

    return rax - arg1;
}

int64_t __convention("win64") sub_1110(int64_t arg1)
{
    int64_t result = 0;

    if (!arg1)
        return 0;

    while (*(arg1 + (result << 1)))
        result += 1;

    return result;
}

int64_t __convention("win64") sub_1130(char* arg1)
{
    int32_t result = 0;

    while (true)
    {
        int32_t rdx_1 = *arg1;

        if (rdx_1 - 0x30 > 9)
            break;

        arg1 = &arg1[1];
        result = result * 0xa + rdx_1 - 0x30;
    }

    return result;
}

char* __convention("win64") sub_1150(char* arg1, char* arg2)
{
    char* result = arg1;
    char* r9 = arg1;

    while (*r9)
        r9 = &r9[1];

    int64_t r8 = 0;

    while (true)
    {
        arg1 = arg2[r8];

        if (!arg1)
            break;

        r9[r8] = arg1;
        r8 += 1;
    }

    r9[r8] = 0;
    return result;
}

uint64_t __convention("win64") sub_1180(char* arg1, int64_t arg2, char* arg3, int64_t arg4)
{
    if (!(!arg3 | !arg2))
    {
        int64_t r10_1 = 0;

        if (arg1)
        {
            while (arg1[r10_1])
            {
                r10_1 += 1;

                if (r10_1 >= arg2)
                    break;
            }

            if (arg2 != r10_1)
            {
                char* rcx = &arg1[r10_1];
                int64_t rax_2 = 0;

                while (true)
                {
                    if (rax_2 == arg4)
                    {
                        *rcx = 0;
                        break;
                    }

                    if (rax_2 + r10_1 < arg2 - 1)
                    {
                        int64_t r11_1;
                        r11_1 = arg3[rax_2];

                        if (r11_1)
                        {
                            *rcx = r11_1;
                            rax_2 += 1;
                            rcx = &rcx[1];
                            continue;
                        }
                    }

                    *rcx = 0;

                    if (rax_2 >= arg4)
                        break;

                    rax_2 = arg3[rax_2];
                    return rax_2;
                }

                return 0;
            }
        }
    }

    return 1;
}

int64_t __convention("win64") sub_1200(char* arg1, int64_t arg2, char* arg3, int64_t arg4)
{
    arg2 = arg2 < arg4;

    if (!(!arg3 | arg2))
    {
        int64_t i = 0;

        if (arg1)
        {
            for (; i != arg4; i += 1)
            {
                arg2 = arg3[i];
                arg1[i] = arg2;
            }

            return 0;
        }
    }

    return 1;
}

char* __convention("win64") sub_1240(int32_t arg1, char* arg2, int32_t arg3)
{
    if (arg3 - 2 > 0x22)
    {
        *arg2 = 0;
        return arg2;
    }

    int32_t rax_1 = arg1;
    int32_t rdx;
    rdx = arg3 == 0xa;
    rdx &= arg1 >> 0x1f;

    if (rdx)
        rax_1 = -(rax_1);

    char* rcx_1 = arg2;
    char* rdx_3;

    while (true)
    {
        int32_t temp2_1;
        int32_t temp3_1;
        temp2_1 = HIGHD(rax_1);
        temp3_1 = LOWD(rax_1);
        int32_t temp1_1 = COMBINE(temp2_1, temp3_1) % arg3;
        rax_1 = COMBINE(temp2_1, temp3_1) / arg3;
        char r11_1 = temp1_1 + 0x57;

        if (temp1_1 <= 9)
            r11_1 = temp1_1 + 0x30;

        rdx_3 = &rcx_1[1];
        rdx_3[-1] = r11_1;

        if (!rax_1)
            break;

        rcx_1 = rdx_3;
    }

    if (rdx)
    {
        *rdx_3 = 0x2d;
        rcx_1 = rdx_3;
        rdx_3 = &rcx_1[2];
    }

    *rdx_3 = 0;
    char* rax_4 = arg2;

    while (rax_4 < rcx_1)
    {
        rdx_3 = *rcx_1;
        arg3 = *rax_4;
        rax_4 = &rax_4[1];
        rcx_1 -= 1;
        rcx_1[1] = arg3;
        rax_4[-1] = rdx_3;
    }

    return arg2;
}

char* __convention("win64") sub_12d0(char* arg1, int64_t arg2)
{
    for (int64_t i = 0; arg2 != i; i += 1)
        arg1[i] = 0;

    return arg1;
}

uint64_t __convention("win64") sub_12f0(void* arg1, void* arg2, int64_t arg3)
{
    int64_t r9 = 0;
    uint32_t rax_1;
    uint32_t r10_1;

    while (true)
    {
        if (r9 == arg3)
            return 0;

        rax_1 = *(arg1 + r9);
        r10_1 = *(arg2 + r9);

        if (rax_1 != r10_1)
            break;

        r9 += 1;
    }

    return rax_1 - r10_1;
}

int64_t __convention("win64") sub_1320(char* arg1, char* arg2, int64_t arg3)
{
    int64_t i;

    for (i = 0; i != arg3; i += 1)
        arg1[i] = arg2[i] ^ *(&data_1329 + (i & 7));

    return i;
}

int64_t sub_1350(int64_t arg1, int64_t arg2, int64_t arg3, void* arg4)
{
    int64_t rbx = *(arg4 + 0x70);
    int64_t rax;
    int64_t rsi_1;
    rax = (*(arg4 + 0x68))(arg1, arg3);
    /* jump -> rbx */
}

int64_t __convention("win64") sub_1380(void* arg1, int64_t arg2, int64_t arg3)
{
    int64_t rbx = *(arg1 + 0x80);
    int64_t rax;
    int64_t rsi_1;
    int64_t rdi_1;
    rax = (*(arg1 + 0x68))(arg3, arg2);
    /* jump -> rbx */
}

int64_t sub_13b0(int64_t arg1, int64_t arg2, int64_t arg3, void* arg4)
{
    int64_t rbx = *(arg4 + 0x78);
    int64_t rax;
    int64_t rsi_1;
    rax = (*(arg4 + 0x68))(arg1, arg3);
    /* jump -> rbx */
}

uint64_t __convention("win64") sub_13e0(int32_t arg1, int64_t* arg2, int64_t* arg3, int64_t* arg4)
{
    int64_t r8;
    int64_t arg_18 = r8;
    int32_t var_6c = 0x46e183fa;
    char var_68 = 0x14;
    int64_t var_50 = 0x26f31b88d7459a3e;
    int64_t var_58 = 0x7f51121412b2ccaa;
    char var_67;
    int64_t i;

    for (i = 0; i != 5; i += 1)
        (&var_67)[i] = *(&var_6c + i) ^ *(i + &var_58);

    i = var_67;
    int32_t var_74 = 0x12e689ed;
    int64_t var_50_1 = 0x26f31b88d7459a3e;
    int16_t var_62 = i;
    char var_66;
    i = var_66;
    int16_t var_60 = i;
    char var_65;
    i = var_65;
    int16_t var_5e = i;
    char var_64;
    i = var_64;
    int16_t var_5c = i;
    char var_63;
    i = var_63;
    int16_t var_5a = i;
    var_58 = 0x7f51121412b2ccaa;
    char var_70;
    int64_t i_1;

    for (i_1 = 0; i_1 != 4; i_1 += 1)
        (&var_70)[i_1] = *(&var_74 + i_1) ^ *(&var_58 + i_1);

    i_1 = var_70;
    var_58 = i_1;
    char var_6f;
    i_1 = var_6f;
    *(&var_58 + 2) = i_1;
    char var_6e;
    i_1 = var_6e;
    *(&var_58 + 4) = i_1;
    char var_6d;
    i_1 = var_6d;
    *(&var_58 + 6) = i_1;
    void* rax = sub_f70(arg2[8], 0xaebc83a5);
    void* rax_1 = sub_f70(arg2[8], 0xb0b51a4d);
    void* rax_2 = sub_f70(arg2[8], 0x1552df72);
    void* rax_3 = sub_f70(arg2[8], 0xe0cfb564);
    void* rax_4 = sub_f70(arg2[8], 0xec3c8021);
    void* rax_5 = sub_f70(arg2[8], 0x26088ae6);
    void* rax_6 = sub_f70(arg2[8], 0x943a5129);
    void* rax_7 = sub_f70(arg2[8], 0xd2053a99);
    int32_t var_d8 = 0;
    int32_t rsi_1 = 1;

    if (rax())
    {
        if (rax_1())
        {
            __builtin_memset(&var_d8, 0, 0x14);
            int64_t rax_10;
            int32_t rdi_1;
            rax_10 = rax_2();

            if (rax_10)
            {
                int64_t var_d0;
                var_d0 = rdi_1;
                int32_t var_c8;
                var_c8 = 0;
                int32_t var_d8_1 = rdi_1;

                if (rax_3() && rax_4())
                {
                    while (true)
                    {
                        int32_t rax_13;
                        int64_t rsi_2;
                        int64_t rdi_2;
                        rax_13 = rax_5();

                        if (!rax_13)
                            break;

                        uint64_t rdx_2 = 0;

                        if (!rdx_2)
                            break;

                        int64_t rax_14 = *arg3;
                        int64_t rax_15;

                        if (rax_14)
                            rax_15 = sub_1380(arg2, rax_14, rdx_2 + *arg4);
                        else
                            rax_15 = sub_1350(rdi_2, rsi_2, rdx_2, arg2);

                        *arg3 = rax_15;

                        if (!rax_15)
                            break;

                        if (!rax_6())
                            break;

                        *arg4 = *arg4;
                    }
                }

                rax_7();
            }

            rax_7();
        }

        rsi_1 = rax_7();
    }

    return rsi_1;
}

int64_t __convention("win64") sub_1770(void* arg1, void* arg2, void* arg3)
{
    void* r15 = arg2;
    void* rbx = arg3 + r15;
    void* rax = sub_f70(*(arg1 + 0x30), 0x27c5f681);
    void* rax_1 = sub_f70(*(arg1 + 0x30), 0xee9d4374);
    void* rax_2 = sub_f70(*(arg1 + 0x30), 0xebcdfe95);
    char result = rax_2(sub_f70(*(arg1 + 0x30), 0x2fa62ca8), rax_1);
    char result_1 = result;

    while (r15 != rbx)
    {
        int64_t rdi_2 = rax()();
        int32_t var_58;
        char var_54;
        int32_t var_50;
        char var_4c;
        char rax_9 = var_54 ^ var_58 ^ var_50 ^ var_4c ^ result_1 ^ r15;
        r15 += 1;
        *(r15 - 1) = rax_9;
        result = rdi_2();
    }

    return result;
}

int64_t (*)() __convention("win64") sub_1830(void* arg1, void* arg2, int64_t arg3, int32_t arg4)
{
    int64_t rbp = 0;
    int64_t rbx = arg3;
    void* rsi_1;

    while (true)
    {
        if (rbp >= *(*(arg1 + 0x3c) + arg1 + 0x50) - rbx)
            return sub_0;

        rsi_1 = arg1 + rbp;

        if (!sub_12f0(rsi_1, arg2, rbx))
            break;

        rbp += 1;
    }

    if (arg4)
        rbx = 0;

    return rsi_1 + rbx;
}

void* __convention("win64") sub_18a0(void* arg1)
{
    void* result = sub_f70(*(arg1 + 0x30), 0x71948ca4);

    if (!result)
        return result;

    /* jump -> result */
}

