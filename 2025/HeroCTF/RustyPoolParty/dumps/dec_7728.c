int64_t sub_0()
{
    int64_t var_127;
    __builtin_strcpy(&var_127, "FLAG PART_3: oL_P4r7Y}");
    void var_d0;
    __builtin_memset(&var_d0, 0, 0x88);

    if (sub_ee0(&var_d0))
        return 1;

    void* var_a0;
    void* rax_2 = sub_14b0(var_a0, 0xa215c401);
    void* rax_3 = sub_14b0(var_a0, 0x58d5d3e6);
    void* rax_4 = sub_14b0(var_a0, 0x8a851d20);
    void* rax_5 = sub_14b0(var_a0, 0x54fcc943);
    void* rax_6 = sub_14b0(var_a0, 0x7f07c44a);
    void* rax_7 = sub_14b0(var_a0, 0xfaba0065);
    sub_14b0(var_a0, 0xe53f7a31);
    sub_14b0(var_a0, 0x5056df37);
    int64_t rax_9;
    int64_t rdx;
    int64_t* rsi_2;
    int64_t rdi_1;
    int64_t r8;
    rax_9 = sub_14b0(var_a0, 0xf9d2dde2)(rax_2, &var_d0, 1, 0, 0, 0);

    if (!rax_9)
    {
        sub_a90(rdi_1, rsi_2, rdx, rsi_2, r8);
        void* rax_10 = sub_1560(0xa3e6f6c3);

        if (rax_10)
        {
            void* rax_11 = sub_14b0(rax_10, 0xf9d2dde2);
            void* rax_12 = sub_14b0(rax_10, 0x71948ca4);

            if (rax_11 && rax_12 && rax_11())
                rax_12();
        }

        while (true)
            /* nop */

        return;
    }

    int64_t var_13f = 0x26817efca424f762;
    int64_t var_e8 = 0x26f31b88d7459a3e;
    int64_t var_147 = 0x1a217b644e9c90f6;
    int64_t var_f0 = 0x7f51121412b2ccaa;

    for (int64_t i = 0; i != 0x10; i += 1)
    {
        char var_137[0xf];
        var_137[i] = *(&var_147 + i) ^ *(&var_f0 + i);
    }

    int32_t var_220 = 0x2000;
    int64_t var_210 = 0;
    int32_t var_218 = 0;
    int32_t var_228 = 0x2000;
    int64_t rax_14 = rdi_1();
    int64_t var_200 = rax_14;

    if (rax_14 == -1)
    {
        int64_t rdx_2;
        int64_t* rsi_4;
        int64_t rdi_2;
        int64_t r8_1;
        rdx_2 = rax_7();
        sub_a90(rdi_2, rsi_4, rdx_2, rsi_4, r8_1);
        void* rax_16 = sub_1560(0xa3e6f6c3);

        if (rax_16)
        {
            void* rax_17 = sub_14b0(rax_16, 0xf9d2dde2);
            void* rax_18 = sub_14b0(rax_16, 0x71948ca4);

            if (rax_17 && rax_18 && rax_17())
                rax_18();
        }

        while (true)
            /* nop */

        return;
    }

    int64_t var_f8 = rax_9;
    void var_110;
    sub_1de0(rax_3(__builtin_memset(&var_110, 0, 0x18)), rax_9);
    int32_t var_1c8 = 0;
    var_228 = 0;
    rax_5();
    char var_1c0;

    if (var_1c8 == 5 && var_1c0 == 1)
    {
        rax_4();

        while (true)
        {
            int64_t var_1b1 = 0x1a217b644e9c90f6;
            *(&var_1b1 + 5) = -0x7745d5069de5de85;
            void var_1a4;
            sub_e20(&var_1b1, &var_1a4);

            if (sub_d50(&var_1a4, var_a0) == -1)
                break;

            char var_1bb = 2;
            int32_t var_1ba_1 = 0;
            int32_t var_1c4 = 0;
            var_228 = 0;
            rax_6();
            var_228 = 0;
            int64_t rsi_9;
            int64_t rdi_5;
            rsi_9 = rax_5();

            if (var_1c8 == 5 && var_1c0 == 3)
            {
                int32_t var_1bf;
                char* rax_26 = sub_1890(rdi_5, rsi_9, var_1bf, &var_d0);

                if (rax_26)
                {
                    var_228 = 0;

                    if (rax_5())
                    {
                        char* rsi_10;
                        void* rdi_6;
                        rsi_10 = rax_7();

                        if (var_1bf <= 1)
                        {
                        label_500:
                            sub_18f0(rdi_6, rsi_10, rax_26, &var_d0);
                            break;
                        }

                        char count_1 = *rax_26;

                        if (count_1 - 1 > 0x1f)
                            goto label_500;

                        uint32_t count_2 = count_1;

                        if (count_2 + 1 >= var_1bf)
                            goto label_500;

                        uint64_t count = count_1;
                        int32_t rax_30 = var_1bf - 1 - count_2;
                        uint64_t r9_1 = rax_30;
                        int64_t rsi_12;
                        int64_t rdi_7;
                        rdi_7 = __builtin_memcpy(&var_f0, &rax_26[1], count);
                        sub_b00(&rax_26[1], count, &rax_26[count + 1], r9_1);

                        if (!r9_1)
                            sub_18f0(rdi_7, rsi_12, rax_26, &var_d0, &rax_26[count + 1], r9_1);
                        else
                        {
                            int64_t var_197;
                            char var_18a;
                            int64_t var_17d;
                            char var_170;
                            int64_t var_163;
                            void var_155;

                            if (rax_26[count + 1] != 0xff)
                            {
                                char* rax_34;
                                rax_34 = sub_1890(rdi_7, rsi_12, r9_1, &var_d0, &rax_26[count + 1]);

                                if (!rax_34)
                                {
                                    sub_18f0(rdi_6, rsi_10, rax_26, &var_d0);
                                    break;
                                }

                                int64_t rax_35 = 0;

                                do
                                {
                                    rax_34[rax_35] = rax_26[count + 1 + rax_35];
                                    rax_35 += 1;
                                } while (rax_35 < r9_1);

                                sub_18f0(rax_34, rsi_10, rax_26, &var_d0);
                                var_163 = 0x1a217b644e9c90f6;
                                *(&var_163 + 6) = 0x1bedbb2cfc621a21;
                                sub_ea0(&var_163, &var_155);
                                int64_t rax_36 = sub_d50(&var_155, var_a0);

                                if (rax_36 == -1)
                                    break;

                                var_228 = 0;
                                var_197 = 4;
                                *(&var_197 + 1) = rax_30;
                                rax_6(rax_36);
                                var_228 = 0;
                                rax_6();
                                var_228 = 0;
                                int64_t rdi_12 = rax_5();

                                if (var_1c8 == 5 && var_1c0 == 5)
                                {
                                    if (var_1bf && sub_1890(rdi_12, 0, var_1bf, &var_d0))
                                    {
                                        var_228 = 0;
                                        rax_5();
                                    }

                                    int64_t rsi_16;
                                    void* rdi_14;
                                    rsi_16 = rax_7(&var_d0);
                                    rsi_10 = sub_18f0(rdi_14, rsi_16, rax_34, rdi_14);
                                    uint64_t r9_5 = var_1bf;

                                    if (r9_5 && rsi_10)
                                        sub_b00(&var_f0, count, rsi_10, r9_5);

                                    var_17d = 0x1a217b644e9c90f6;
                                    *(&var_17d + 5) = -0x7745d5069de5de85;
                                    sub_e20(&var_17d, &var_170);

                                    if (sub_d50(&var_170, var_a0) != -1)
                                    {
                                        var_18a = 6;
                                        var_228 = 0;
                                        int32_t var_189_1 = var_1bf;
                                        int64_t rsi_17;
                                        void* rdi_15;
                                        rsi_17 = rax_6();

                                        if (!var_1bf)
                                        {
                                            if (rsi_17)
                                                sub_18f0(rdi_15, rsi_17, rsi_17, rdi_15);
                                        }
                                        else if (rsi_17)
                                        {
                                            var_228 = 0;
                                            rsi_17 = rax_6();
                                            sub_18f0(rdi_15, rsi_17, rsi_17, rdi_15);
                                        }

                                        rax_7();
                                        continue;
                                    }
                                    else if (!rsi_10)
                                        break;

                                    sub_18f0(rdi_6, rsi_10, rsi_10, rdi_6);
                                    break;
                                }
                            }
                            else
                            {
                                char* rsi_14 = sub_18f0(rdi_7, &var_170, rax_26, &var_d0,
                                    &rax_26[count + 1], r9_1);
                                var_163 = 0x1a217b644e9c90f6;
                                *(&var_163 + 6) = 0x1bedbb2cfc621a21;
                                sub_ea0(&var_163, &var_155);
                                int64_t rax_31 = sub_d50(&var_155, var_a0);

                                if (rax_31 != -1)
                                {
                                    var_170 = 7;
                                    var_228 = 0;
                                    int32_t var_16f_1 = 0;
                                    rax_6(rax_31);
                                    rsi_14 = rax_7();
                                }

                                var_197 = 0x1a217b644e9c90f6;
                                *(&var_197 + 5) = -0x7745d5069de5de85;
                                sub_e20(&var_197, &var_18a);
                                int64_t rax_32 = sub_d50(&var_18a, var_a0);

                                if (rax_32 != -1)
                                {
                                    var_228 = 0;
                                    var_170 = 6;
                                    int32_t var_16f_2 = 0;
                                    rax_6(rax_32);
                                    rsi_14 = rax_7();
                                }

                                var_17d = 0x1a217b644e9c90f6;
                                *(&var_17d + 5) = -0x7745d5069de5de85;
                                sub_e20(&var_17d, rsi_14);
                                int64_t rax_33 = sub_d50(rsi_14, var_a0);

                                if (rax_33 == -1)
                                    break;

                                char var_1b6 = 7;
                                int32_t var_1b5_1 = 0;
                                var_228 = 0;
                                rax_6(0, rax_33, &var_1b6, rax_33, 5, &var_1c4);
                            }
                        }
                    }
                }
            }

            rax_7();
            break;
        }

        rax_7();
        int64_t rdx_30;
        int64_t rsi_18;
        int64_t rdi_16;
        int64_t r8_9;
        rdx_30 = rax_7();
        sub_a90(rdi_16, rsi_18, rdx_30, &var_d0, r8_9);
        void* rax_41 = sub_1560(0xa3e6f6c3);

        if (rax_41)
        {
            void* rax_42 = sub_14b0(rax_41, 0xf9d2dde2);
            void* rax_43 = sub_14b0(rax_41, 0x71948ca4);

            if (rax_42 && rax_43 && rax_42())
                rax_43();
        }

        while (true)
            /* nop */
    }

    rax_4();
    int64_t rdx_4;
    int64_t* rsi_7;
    int64_t rdi_4;
    int64_t r8_2;
    rdx_4 = rax_7();
    sub_a90(rdi_4, rsi_7, rdx_4, rsi_7, r8_2);
    void* rax_21 = sub_1560(0xa3e6f6c3);

    if (rax_21)
    {
        void* rax_22 = sub_14b0(rax_21, 0xf9d2dde2);
        void* rax_23 = sub_14b0(rax_21, 0x71948ca4);

        if (rax_22 && rax_23 && rax_22())
            rax_23();
    }

    while (true)
        /* nop */
}

void sub_a90(int64_t arg1, int64_t arg2, int64_t arg3, int64_t* arg4, int64_t arg5)
{
    int64_t rdx = *arg4;
    int64_t rax;

    if (rdx)
    {
        rax = sub_18f0(arg1, arg2, rdx, arg4);
        arg5 = 0;
        *arg4 = 0;
    }

    int64_t rdx_1 = arg4[1];

    if (rdx_1)
    {
        rax = sub_18f0(arg1, arg2, rdx_1, arg4, arg5);
        arg4[1] = 0;
    }

    int64_t rdx_2 = arg4[2];

    if (rdx_2)
    {
        rax = sub_18f0(arg1, arg2, rdx_2, arg4);
        arg4[2] = 0;
    }

    int64_t rdx_3 = arg4[3];

    if (rdx_3)
    {
        sub_18f0(arg1, arg2, rdx_3, arg4);
        arg4[3] = 0;
    }
}

uint64_t __convention("win64") sub_b00(int64_t arg1, int64_t arg2, char* arg3, int64_t arg4)
{
    int64_t rdi;
    int64_t var_8 = rdi;
    char var_11a[0x102];

    for (int64_t i = 0; i != 0x100; i += 1)
        var_11a[i] = i;

    char (* r10)[0x102] = &var_11a;
    int64_t i_1 = 0;
    int32_t rbx = 0;
    uint64_t result;

    do
    {
        int64_t i_3 = i_1;
        rdi = *r10;
        i_1 += 1;
        r10 = &(*r10)[1];
        uint32_t rax;
        rax = *(arg1 + COMBINE(0, i_3) % arg2);
        rbx += rax + rdi;
        result = rbx;
        uint64_t rdx_1;
        rdx_1 = var_11a[result];
        (*r10)[-1] = rdx_1;
        var_11a[result] = rdi;
    } while (i_1 != 0x100);

    int32_t r10_1 = 0;

    for (int64_t i_2 = 0; arg4 != i_2; i_2 += 1)
    {
        uint64_t rcx_1 = i_2 + 1;
        result = var_11a[rcx_1];
        r10_1 += result;
        uint64_t r11_1 = r10_1;
        rbx = var_11a[r11_1];
        var_11a[rcx_1] = rbx;
        var_11a[r11_1] = result;
        result += var_11a[rcx_1];
        result = var_11a[result];
        arg3[i_2] ^= result;
    }

    return result;
}

void* __convention("win64") sub_bb0(int64_t arg1, void* arg2)
{
    void* rax = sub_14b0(arg2, 0xbdcac9ce);
    void* rax_1 = sub_14b0(arg2, 0x7f07c44a);
    void* rax_2 = sub_14b0(arg2, 0xfaba0065);
    void* r12 = sub_14b0(arg2, 0xb7f5e1c2);
    void* result;
    result = !rax;
    result |= !rax_1;

    if (!result && rax_2)
    {
        int64_t var_76;
        __builtin_memcpy(&var_76,
            "\xe9\xf6\xee\x47\x67\x77\x23\x0c\x62\xe8\x2a\xb8\xfc\x47\x9e\x47\xd9\xb8\xd7\x60\x4b\x76\x"
        "34\x1d\x4b\xfd\x6b\xa3\xf0\x6f\xf3",
            0x1f);
        int64_t var_80_1 = 0x26f31b88d7459a3e;
        int64_t var_88 = 0x7f51121412b2ccaa;
        char var_57[0x27];

        for (int64_t i = 0; i != 0x1f; i += 1)
        {
            uint64_t rdx_2;
            rdx_2 = *(&var_88 + (i & 0xf));
            rdx_2 ^= *(&var_76 + i);
            var_57[i] = rdx_2;
        }

        int32_t var_a0_1 = 0x80;
        int64_t var_98_1 = 0;
        int32_t var_a8_1 = 4;
        int64_t rsi_1;
        int64_t rdi_1;
        result = rax(rax_1, arg1, 0x40000000, &var_57, 1, 0);

        if (result != -1)
        {
            if (r12)
                rsi_1 = r12();

            int32_t r8_1 = 0;
            var_88 = 0;

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

int64_t __convention("win64") sub_d50(int64_t arg1, void* arg2)
{
    void* rax = sub_14b0(arg2, 0xbdcac9ce);
    int64_t r12;
    r12 = sub_14b0(arg2, 0x2fa62ca8);
    int32_t rbx_1 = 0;
    int64_t result;

    while (true)
    {
        int32_t var_40_1 = 0;
        int64_t var_38_1 = 0;
        int32_t var_48_1 = 3;
        int64_t rsi_1;
        result = rax();

        if (result != -1)
            break;

        bool cond:1_1 = rbx_1 == 9;
        rbx_1 += 1;

        if (!cond:1_1 && r12)
        {
            rsi_1();
            continue;
        }

        if (rbx_1 == 0xa)
            break;
    }

    return result;
}

int64_t __convention("win64") sub_de0(char* arg1, char* arg2)
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

int64_t __convention("win64") sub_e20(char* arg1, char* arg2)
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

int64_t __convention("win64") sub_e60(char* arg1, char* arg2)
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

int64_t __convention("win64") sub_ea0(char* arg1, char* arg2)
{
    int64_t i = 0;
    int64_t var_18 = 0x7f51121412b2ccaa;
    int64_t var_10 = 0x26f31b88d7459a3e;

    do
    {
        arg2[i] = arg1[i] ^ *(&var_18 + i);
        i += 1;
    } while (i != 0xe);

    return i;
}

int64_t __convention("win64") sub_ee0(int64_t* arg1)
{
    arg1[6] = sub_1560(0xa3e6f6c3);
    int64_t rax_1 = sub_1560(0xa62a3b3b);
    void* rcx = arg1[6];
    arg1[5] = rax_1;

    if (rax_1 && rcx)
    {
        void* rax_2 = sub_14b0(rcx, 0x86fe8652);
        void* rcx_1 = arg1[5];
        arg1[0xd] = rax_2;
        void* rax_3 = sub_14b0(rcx_1, 0xb3f819f8);
        void* rcx_2 = arg1[6];
        arg1[0xe] = rax_3;
        void* rax_4 = sub_14b0(rcx_2, 0x29630f3d);
        void* rcx_3 = arg1[5];
        arg1[0xf] = rax_4;
        void* rax_5 = sub_14b0(rcx_3, 0xa05ab779);
        arg1[0x10] = rax_5;

        if (arg1[0xd] && arg1[0xe] && arg1[0xf] && rax_5)
        {
            void* rax_6 = sub_14b0(arg1[6], 0x53b2070f);

            if (rax_6)
            {
                int64_t var_146 = 0x1b7f202760d7bfdf;
                *(&var_146 + 7) = 0x45f6521b;
                int64_t var_5a_1 = 0x26f31b88d7459a3e;
                int64_t var_62 = 0x7f51121412b2ccaa;

                for (int64_t i = 0; i != 0xb; i += 1)
                {
                    char var_13b[0xb];
                    char (* var_188_1)[0xb] = &var_13b;
                    var_13b[i] = *(&var_146 + i) ^ *(i + &var_62);
                }

                int32_t var_128_1 = 0xd729f65a;
                void var_124;
                void* var_190_1 = &var_124;
                int64_t var_130 = 0x512166607adca5dd;
                sub_de0(&var_130, &var_124);
                int64_t var_100 = 0x4d627b6473c4a8cb;
                *(&var_100 + 5) = -0x7744d601efb29d85;
                void var_f3;
                sub_e20(&var_100, &var_f3);
                int64_t var_118 = 0x516321787ed7a4d9;
                int32_t var_110_1 = 0xd729f65a;
                void var_10c;
                sub_de0(&var_118, &var_10c);
                int64_t var_16e = 0x13353c2621dba8cd;
                int16_t var_166_1 = 0x9a52;
                void var_164;
                sub_e60(&var_16e, &var_164);
                int64_t var_15a = 0x13353c797fdca5dd;
                int16_t var_152_1 = 0x9a52;
                void var_150;
                sub_e60(&var_15a, &var_150);
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
                rax_13 = sub_1890(rdi_7, rsi_1, 0x200, arg1);
                *arg1 = rax_13;
                int64_t rax_14;
                int64_t rsi_3;
                int64_t rdi_9;
                rax_14 = sub_1890(rdi_8, rsi_2, 0x100, arg1);
                arg1[1] = rax_14;
                int64_t rax_15;
                int64_t rsi_4;
                int64_t rdi_10;
                rax_15 = sub_1890(rdi_9, rsi_3, 0x50, arg1);
                arg1[2] = rax_15;
                int64_t rax_16;
                int16_t* rsi_5;
                rax_16 = sub_1890(rdi_10, rsi_4, 0x80, arg1);
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
                            char var_178_1 = 0x3e;
                            int64_t var_74_1 = 0x26f31b88d7459a3e;
                            int64_t var_180 = 0x1b3f73797fddaf85;
                            int64_t var_7c = 0x7f51121412b2ccaa;
                            char var_177[0x9];

                            for (int64_t i_3 = 0; i_3 != 9; i_3 += 1)
                            {
                                int16_t rdx_8;
                                rdx_8 = *(&var_180 + i_3);
                                rdx_8 ^= *(i_3 + &var_7c);
                                var_177[i_3] = rdx_8;
                            }

                            int128_t var_8e;
                            int64_t i_4;

                            for (i_4 = 0; i_4 != 9; i_4 += 1)
                                *(&var_8e + (i_4 << 1)) = var_177[i_4];

                            int16_t var_7e;
                            i_4 = var_7e;
                            int128_t zmm0_1 = var_8e;
                            rcx_14[1] = i_4;
                            int64_t var_e6 = 0xb3f777353f498e9;
                            *rcx_14 = zmm0_1;
                            *(&var_e6 + 5) = -0x77189454eef4c089;
                            char var_d9[0xd];
                            sub_e20(&var_e6, &var_d9);

                            for (int64_t i_5 = 0; i_5 != 0xd; i_5 += 1)
                            {
                                char (* rdx_9)[0xd];
                                rdx_9 = var_d9[i_5];
                                *(&var_7c + (i_5 << 1)) = rdx_9;
                            }

                            int128_t zmm1_1 = var_7c;
                            int64_t var_cc = 0x1b3e71787ed7a4d9;
                            *rdi_11 = zmm1_1;
                            *(rdi_11 + 0xa) = *(&var_74_1 + 2);
                            *(&var_cc + 6) = 0x1be6be27b45b1b3e;
                            char var_be[0xe];
                            sub_ea0(&var_cc, &var_be);

                            for (int64_t i_6 = 0; i_6 != 0xe; i_6 += 1)
                            {
                                int64_t* rcx_16;
                                rcx_16 = var_be[i_6];
                                arg1[3][i_6] = rcx_16;
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

int64_t sub_13d0()
{
    void* gsbase;
    return *(gsbase + 0x30);
}

void* sub_13e0()
{
    void* gsbase;
    void* result = *(gsbase + 0x30);

    if (!result)
        return result;

    return *(result + 0x60);
}

int64_t __convention("win64") sub_1400(int64_t arg1, int64_t arg2, char* arg3)
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

uint64_t __convention("win64") sub_1430(char* arg1, int32_t arg2)
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

int64_t __convention("win64") sub_1480(char* arg1, int32_t arg2)
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

void* __convention("win64") sub_14b0(void* arg1, int32_t arg2)
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

            if (sub_1480(r14_1 + arg1, sub_1630(r14_1 + arg1)) == arg2)
                return *(rdi_1 + arg1 + (*(rbp_1 + arg1 + (i << 1)) << 2)) + arg1;

            r12_2 = &r12_2[1];
        }
    }

    return sub_0;
}

int64_t __convention("win64") sub_1560(int32_t arg1)
{
    char var_428[0x400];
    __builtin_memset(&var_428, 0, 0x400);
    void* rax = sub_13e0();

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
                            sub_1400(rcx, rdx_1, &var_428);

                            if (sub_1480(&var_428, r11_1) == arg1)
                            {
                                int64_t result = rbx_1[4];
                                sub_1810(&var_428, 0x400);
                                return result;
                            }

                            sub_1810(&var_428, 0x400);
                        }
                    }
                }

                rbx_1 = *rbx_1;
            }
        }
    }

    return 0;
}

void* __convention("win64") sub_1630(char* arg1)
{
    char* rax = arg1;

    while (*rax)
        rax = &rax[1];

    return rax - arg1;
}

int64_t __convention("win64") sub_1650(int64_t arg1)
{
    int64_t result = 0;

    if (!arg1)
        return 0;

    while (*(arg1 + (result << 1)))
        result += 1;

    return result;
}

int64_t __convention("win64") sub_1670(char* arg1)
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

char* __convention("win64") sub_1690(char* arg1, char* arg2)
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

uint64_t __convention("win64") sub_16c0(char* arg1, int64_t arg2, char* arg3, int64_t arg4)
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

int64_t __convention("win64") sub_1740(char* arg1, int64_t arg2, char* arg3, int64_t arg4)
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

char* __convention("win64") sub_1780(int32_t arg1, char* arg2, int32_t arg3)
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

char* __convention("win64") sub_1810(char* arg1, int64_t arg2)
{
    for (int64_t i = 0; arg2 != i; i += 1)
        arg1[i] = 0;

    return arg1;
}

uint64_t __convention("win64") sub_1830(void* arg1, void* arg2, int64_t arg3)
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

int64_t __convention("win64") sub_1860(char* arg1, char* arg2, int64_t arg3)
{
    int64_t i;

    for (i = 0; i != arg3; i += 1)
        arg1[i] = arg2[i] ^ *(&data_1869 + (i & 7));

    return i;
}

int64_t sub_1890(int64_t arg1, int64_t arg2, int64_t arg3, void* arg4)
{
    int64_t rbx = *(arg4 + 0x70);
    int64_t rax;
    int64_t rsi_1;
    rax = (*(arg4 + 0x68))(arg1, arg3);
    /* jump -> rbx */
}

int64_t __convention("win64") sub_18c0(void* arg1, int64_t arg2, int64_t arg3)
{
    int64_t rbx = *(arg1 + 0x80);
    int64_t rax;
    int64_t rsi_1;
    int64_t rdi_1;
    rax = (*(arg1 + 0x68))(arg3, arg2);
    /* jump -> rbx */
}

int64_t sub_18f0(int64_t arg1, int64_t arg2, int64_t arg3, void* arg4)
{
    int64_t rbx = *(arg4 + 0x78);
    int64_t rax;
    int64_t rsi_1;
    rax = (*(arg4 + 0x68))(arg1, arg3);
    /* jump -> rbx */
}

int64_t __convention("win64") sub_1cb0(void* arg1, void* arg2, void* arg3)
{
    void* r15 = arg2;
    void* rbx = arg3 + r15;
    void* rax = sub_14b0(*(arg1 + 0x30), 0x27c5f681);
    void* rax_1 = sub_14b0(*(arg1 + 0x30), 0xee9d4374);
    void* rax_2 = sub_14b0(*(arg1 + 0x30), 0xebcdfe95);
    char result = rax_2(sub_14b0(*(arg1 + 0x30), 0x2fa62ca8), rax_1);
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

int64_t (*)() __convention("win64") sub_1d70(void* arg1, void* arg2, int64_t arg3, int32_t arg4)
{
    int64_t rbp = 0;
    int64_t rbx = arg3;
    void* rsi_1;

    while (true)
    {
        if (rbp >= *(*(arg1 + 0x3c) + arg1 + 0x50) - rbx)
            return sub_0;

        rsi_1 = arg1 + rbp;

        if (!sub_1830(rsi_1, arg2, rbx))
            break;

        rbp += 1;
    }

    if (arg4)
        rbx = 0;

    return rsi_1 + rbx;
}

void* __convention("win64") sub_1de0(void* arg1)
{
    void* result = sub_14b0(*(arg1 + 0x30), 0x71948ca4);

    if (!result)
        return result;

    /* jump -> result */
}

