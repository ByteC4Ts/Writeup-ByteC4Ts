int64_t sub_0()
{
    int64_t var_130a;
    __builtin_strcpy(&var_130a, "FLAG PART_2: t_KiNd_0F_P0");

    if (var_130a == 0x58)
        return 0;

    void var_12d0;
    __builtin_memset(&var_12d0, 0, 0x88);

    if (sub_d90(&var_12d0))
        return 1;

    void* var_12a0;
    void* rax_3 = sub_1360(var_12a0, 0xa215c401);
    void* rax_4 = sub_1360(var_12a0, 0x58d5d3e6);
    void* rax_5 = sub_1360(var_12a0, 0x8a851d20);
    void* rax_6 = sub_1360(var_12a0, 0x54fcc943);
    void* rax_7 = sub_1360(var_12a0, 0x7f07c44a);
    void* rax_8 = sub_1360(var_12a0, 0xbdcac9ce);
    void* rax_9 = sub_1360(var_12a0, 0x44ed8118);
    void* rax_10 = sub_1360(var_12a0, 0xfaba0065);
    sub_1360(var_12a0, 0xe53f7a31);
    void* rax_11 = sub_1360(var_12a0, 0xafd195a6);
    void* rax_12 = sub_1360(var_12a0, 0xf9d2dde2);
    void* rax_13 = sub_1360(var_12a0, 0x68fe748);
    int64_t rax_14;
    int64_t rdx;
    int64_t rsi_1;
    int64_t rdi_1;
    int64_t r8;
    rax_14 = rax_12(rax_3, var_12a0, 1, 0, 0, 0);

    if (!rax_14)
    {
        sub_c20(rdi_1, rsi_1, rdx, &var_12d0, r8);
        void* rax_15 = sub_1410(0xa3e6f6c3);

        if (rax_15)
        {
            void* rax_16 = sub_1360(rax_15, 0xf9d2dde2);
            void* rax_17 = sub_1360(rax_15, 0x71948ca4);

            if (rax_16 && rax_17 && rax_16())
                rax_17();
        }

        while (true)
            /* nop */

        return;
    }

    int64_t var_1326 = 0x1a217b644e9c90f6;
    *(&var_1326 + 6) = 0x1bedbb2cfc621a21;
    void var_1318;
    sub_d50(&var_1326, &var_1318);
    int32_t var_13d8 = 0;
    int64_t var_13d0 = 0;
    int32_t var_13e0 = 0x1000;
    int32_t var_13e8 = 0x1000;

    if (rdi_1() == -1)
    {
        int64_t rdx_2;
        int64_t rsi_3;
        int64_t rdi_2;
        int64_t r8_1;
        rdx_2 = rax_10();
        sub_c20(rdi_2, rsi_3, rdx_2, &var_12d0, r8_1);
        void* rax_20 = sub_1410(0xa3e6f6c3);

        if (rax_20)
        {
            void* rax_21 = sub_1360(rax_20, 0xf9d2dde2);
            void* rax_22 = sub_1360(rax_20, 0x71948ca4);

            if (rax_21 && rax_22 && rax_21())
                rax_22();
        }

        while (true)
            /* nop */

        return;
    }

    while (true)
    {
        int64_t var_12d8_1 = rax_14;
        void var_12f0;
        rax_4(__builtin_memset(&var_12f0, 0, 0x18));
        sub_1c90(&var_12d0, rax_14);
        int32_t var_1344 = 0;
        var_13e8 = 0;
        rax_6();

        if (var_1344 == 5)
        {
            char var_1335;

            if (var_1335 == 7)  /* "AVAUATUWVS" */
                break;

            if (var_1335 == 4)
            {
                bool var_1248;
                int64_t rdi_5 = __builtin_memset(&var_1248, 0, 0x200);
                int32_t var_1334;

                if (var_1334 - 1 <= 0x1fe)
                {
                    var_13e8 = 0;
                    void* rsi_6 = rax_6(rdi_5);
                    bool rdx_5 = var_1248;
                    uint64_t i_4 = var_1334 - 1;
                    int32_t var_1330;
                    char var_1048;
                    char* rbx_6;
                    int32_t r12_1;
                    char var_1247[0x1ff];
                    int32_t rax_28;

                    if (rdx_5 == 2)
                    {
                        int64_t rdi_12 = 0;
                        int64_t r13_5;
                        bool cond:2_1;

                        do
                        {
                            cond:2_1 = var_1247[rdi_12];
                            r13_5 = rdi_12;
                            rax_28 = rdi_12 < i_4;
                            rdi_12 += 1;
                        } while (cond:2_1 & rax_28);
                        void* rax_52 = sub_1360(rsi_6, 0xf642e4f7);

                        if (!rax_52)
                        {
                            for (int64_t i = 0; i != 0x200; i += 1)
                            {
                                char rdx_15 = var_1247[i];

                                if (!rdx_15)
                                    break;

                                (&var_1048)[i] = rdx_15;
                            }
                        }
                        else
                            rax_52();

                        var_13e0 = 0x80;
                        var_13d8 = 0;
                        var_13e8 = 2;
                        int64_t rax_53;
                        void* rsi_9;
                        int64_t rdi_13;
                        rax_53 = rax_8();

                        if (rax_53 == -1)
                        {
                            r12_1 = 0x19;
                            char* rax_58 = sub_1740(rdi_13, rsi_9, 0x19, &var_12d0);
                            rbx_6 = rax_58;

                            if (rax_58)
                            {
                                for (int64_t i_1 = 0; i_1 != 0x19; i_1 += 1)
                                    rbx_6[i_1] = *(&data_98f + i_1);

                                r12_1 = 0x19;
                            }
                        }
                        else
                        {
                            var_1330 = 0;
                            void* rax_54 = sub_1360(rsi_9, 0x7f07c44a);

                            if (rax_54)
                            {
                                var_13e8 = 0;
                                rax_54();
                            }

                            int64_t rsi_10;
                            int64_t rdi_14;
                            rsi_10 = rax_10();

                            if (var_1330 != i_4 - 1 - r13_5)
                            {
                                r12_1 = 0x14;
                                char* rax_57 = sub_1740(rdi_14, rsi_10, 0x14, &var_12d0);
                                rbx_6 = rax_57;

                                if (rax_57)
                                {
                                    for (int64_t i_2 = 0; i_2 != 0x14; i_2 += 1)
                                        rbx_6[i_2] = *(&data_94d + i_2);

                                    r12_1 = 0x14;
                                }
                            }
                            else
                            {
                                r12_1 = 7;  /* "AVAUATUWVS" */
                                char* rax_56 = sub_1740(rdi_14, rsi_10, 7, &var_12d0);
                                    /* "AVAUATUWVS" */
                                rbx_6 = rax_56;

                                if (rax_56)
                                {
                                    for (int64_t i_3 = 0; i_3 != 7; i_3 += 1)  /* "AVAUATUWVS" */
                                        rbx_6[i_3] = *(&data_911 + i_3);

                                    r12_1 = 7;  /* "AVAUATUWVS" */
                                }
                            }
                        }
                    }
                    else
                    {
                        char var_1408[0x20];
                        void* var_1288;

                        if (rdx_5 > 2)
                        {
                            void* rax_29 = sub_0;

                            if (rdx_5 == 3)
                            {
                                void* r10_1;
                                bool c_2;
                                bool cond:3_1;

                                do
                                {
                                    cond:3_1 = *(&var_1247 + rax_29);
                                    r10_1 = rax_29;
                                    c_2 = rax_29 < i_4;
                                    rax_29 += 1;
                                } while (cond:3_1 & c_2);
                                char* r12_3 = &var_1408 + rax_29 + 0x1c1;
                                int64_t (* rbp_3)() = sub_0;
                                int32_t var_1378_1;

                                do
                                {
                                    rax_29 = *(r12_3 + rbp_3);
                                    var_1378_1 = rbp_3;
                                    rbp_3 += 1;

                                    if (!rax_29)
                                        break;
                                } while (r10_1 + rbp_3 < i_4);

                                char (* rdi_11)[0x1ff] = &var_1247;

                                do
                                {
                                    rax_29 = *rdi_11;

                                    if (!rax_29)
                                        break;

                                    rdi_11 = &(*rdi_11)[1];
                                } while (rax_29 != 0x5c);

                                int32_t var_1350_1 = r10_1;
                                void* var_1358 = sub_1360(var_1288, 0xf6ed1b50);
                                void* rax_50 = sub_1360(var_1288, 0xda5113dc);
                                void* rax_51 = sub_1360(var_1288, 0x1242154a);
                                void* r11_1 = var_1358;
                                void* r13_4 = rax_51;
                                rax_51 = rax_50;

                                if (r11_1 & rax_51 && r13_4)
                                {
                                    var_13d8 = 0;
                                    int32_t* var_13c8_1 = &var_1330;
                                    var_13e8 = 0;
                                    char* var_13d0_1 = &var_1048;
                                    var_13e0 = 0x20006;
                                    int32_t rax_59;
                                    int64_t rsi_11;
                                    int64_t rdi_15;
                                    rax_59 = r11_1();

                                    if (rax_59)
                                    {
                                        r12_1 = 0x18;
                                        char* rax_63 = sub_1740(rdi_15, rsi_11, 0x18, &var_12d0);
                                        rbx_6 = rax_63;

                                        if (rax_63)
                                        {
                                            for (int64_t i_5 = 0; i_5 != 0x18; i_5 += 1)
                                                rbx_6[i_5] = *(&data_b0b + i_5);

                                            r12_1 = 0x18;
                                        }
                                    }
                                    else
                                    {
                                        var_13e8 = rbp_3 + r12_3;
                                        var_13e0 = i_4 - 2 - var_1350_1 - var_1378_1;
                                        int32_t rax_60 = rax_50();
                                        int64_t rsi_12;
                                        int64_t rdi_16;
                                        rsi_12 = r13_4();
                                        void* rcx_41 = &var_12d0;

                                        if (rax_60)
                                        {
                                            r12_1 = 0x17;
                                            char* rax_62 = sub_1740(rdi_16, rsi_12, 0x17, rcx_41);
                                            rbx_6 = rax_62;

                                            if (rax_62)
                                            {
                                                for (int64_t i_6 = 0; i_6 != 0x17; i_6 += 1)
                                                    rbx_6[i_6] = *(&data_acb + i_6);

                                                r12_1 = 0x17;
                                            }
                                        }
                                        else
                                        {
                                            r12_1 = 7;  /* "AVAUATUWVS" */
                                            char* rax_61 = sub_1740(rdi_16, rsi_12, 7, rcx_41);
                                                /* "AVAUATUWVS" */
                                            rbx_6 = rax_61;

                                            if (rax_61)
                                            {
                                                for (int64_t i_7 = 0; i_7 != 7; i_7 += 1)  /* "
                                                        AVAUATUWVS" */
                                                    rbx_6[i_7] = *(&data_a93 + i_7);

                                                r12_1 = 7;  /* "AVAUATUWVS" */
                                            }
                                        }
                                    }
                                }
                                else
                                {
                                    r12_1 = 0;
                                    rbx_6 = sub_0;
                                }
                            }
                            else
                            {
                                r12_1 = 0;
                                rbx_6 = sub_0;
                            }
                        }
                        else
                        {
                            int64_t r13_1 = 0;

                            if (rdx_5)
                            {
                                bool cond:4_1;

                                do
                                {
                                    cond:4_1 = var_1247[r13_1];
                                    rax_28 = r13_1 < i_4;
                                    r13_1 += 1;
                                } while (cond:4_1 & rax_28);
                                char (* rbx_7)[0x1ff] = &var_1247;

                                do
                                {
                                    rax_28 = *rbx_7;

                                    if (!rax_28)
                                        break;

                                    rbx_7 = &(*rbx_7)[1];
                                } while (rax_28 != 0x5c);

                                void* rax_37 = sub_1360(var_1288, 0xdf6a51c);
                                void* rax_38 = sub_1360(var_1288, 0x9027eb7c);
                                void* rbp_2 = sub_1360(var_1288, 0x1242154a);
                                void* rax_39;
                                rax_39 = rax_38;

                                if (!(rax_37 & rax_39) || !rbp_2)
                                {
                                    r12_1 = 0;
                                    rbx_6 = sub_0;
                                }
                                else
                                {
                                    var_13e8 = &var_1330;

                                    if (rax_37())
                                    {
                                        r12_1 = 0;
                                        rbx_6 = sub_0;
                                    }
                                    else
                                    {
                                        int32_t i_8 = 0x1000;
                                        var_13e0 = &i_8;
                                        var_13e8 = &var_1048;
                                        int32_t rax_41;
                                        int64_t rsi_8;
                                        int32_t rdi_8;
                                        rax_41 = rax_38();

                                        if (!rax_41 && i_8)
                                        {
                                            void* rax_42 = sub_14e0(&var_1408[r13_1 + 0x1c1]);
                                            r12_1 = i_8 + rax_42 + rdi_8 + 2;
                                            char* rax_45;
                                            int64_t rdi_9;
                                            rax_45 = sub_1740(rdi_8, rsi_8,
                                                i_8 + rax_42 + rdi_8 + 2, &var_12d0);
                                            rbx_6 = rax_45;

                                            if (!rax_45)
                                            {
                                                r12_1 = 0;
                                                rbx_6 = sub_0;
                                            }
                                            else
                                            {
                                                int64_t rax_46 = 0;

                                                do
                                                {
                                                    rbx_6[rax_46] = var_1247[rax_46];
                                                    rax_46 += 1;
                                                } while (rdi_9 >= rax_46);

                                                int32_t rdi_10 = rdi_9 + 1;
                                                int64_t rax_47 = 0;
                                                char rcx_32;

                                                do
                                                {
                                                    rcx_32 = var_1408[r13_1 + 0x1c1 + rax_47];
                                                    uint64_t rdx_12 = rdi_10;
                                                    rax_47 += 1;
                                                    rdi_10 += 1;
                                                    rbx_6[rdx_12] = rcx_32;
                                                } while (rax_42 >= rax_47);

                                                int64_t rax_48 = 0;

                                                while (rax_48 < i_8)
                                                {
                                                    rcx_32 = (&var_1048)[rax_48];
                                                    uint64_t rdx_13 = rdi_10 + rax_48;
                                                    rax_48 += 1;
                                                    rbx_6[rdx_13] = rcx_32;
                                                }
                                            }
                                        }
                                        else
                                        {
                                            r12_1 = 0;
                                            rbx_6 = sub_0;
                                        }

                                        rbp_2();
                                    }
                                }
                            }
                            else
                            {
                                void* rax_30 = sub_1360(rsi_6, 0xf642e4f7);

                                if (!rax_30)
                                {
                                    for (int64_t i_9 = 0; i_9 != 0x200; i_9 += 1)
                                    {
                                        char rdx_6 = var_1247[i_9];

                                        if (!rdx_6)
                                            break;

                                        (&var_1048)[i_9] = rdx_6;
                                    }
                                }
                                else
                                    rax_30();

                                var_13e8 = 3;
                                var_13d8 = 0;
                                var_13e0 = 0;
                                int64_t rax_31 = rax_8();

                                if (rax_31 == -1)
                                {
                                    r12_1 = 0;
                                    rbx_6 = sub_0;
                                }
                                else
                                {
                                    int32_t rax_32;
                                    int64_t rsi_7;
                                    int64_t rdi_7;
                                    rax_32 = rax_9(rax_31);
                                    void* rax_34;
                                    char* rax_35;

                                    if (rax_32 - 1 <= 0x7fff)
                                    {
                                        rax_34 = sub_14e0(&var_1247);
                                        r12_1 = rax_32 + rax_34 + 1;
                                        rax_35 =
                                            sub_1740(rdi_7, rsi_7, rax_32 + rax_34 + 1, &var_12d0);
                                        rbx_6 = rax_35;
                                    }

                                    if (rax_32 - 1 > 0x7fff || !rax_35)
                                    {
                                        r12_1 = 0;
                                        rbx_6 = sub_0;
                                    }
                                    else
                                    {
                                        int64_t rax_36 = 0;

                                        do
                                        {
                                            rbx_6[rax_36] = var_1247[rax_36];
                                            rax_36 += 1;
                                        } while (rax_34 >= rax_36);

                                        var_13e8 = 0;
                                        rax_6();
                                    }

                                    rax_10();
                                }
                            }
                        }
                    }
                    var_1048 = 5;
                    var_1330 = 0;
                    var_13e8 = 0;
                    int32_t var_1047_1 = r12_1;
                    rax_7();

                    if (r12_1 && rbx_6)
                    {
                        var_13e8 = 0;
                        int64_t rsi_13;
                        int64_t rdi_17;
                        rsi_13 = rax_7();
                        sub_17a0(rdi_17, rsi_13, rbx_6, &var_12d0);
                    }
                }

                rax_11();
                rax_5();
                rax_13();
                continue;
            }
        }

        rax_11();
        rax_5();
    }

    rax_11();
    rax_5();
    rax_10();
    int64_t rdx_4;
    int64_t rsi_5;
    int64_t rdi_4;
    int64_t r8_2;
    rdx_4 = rax_10();
    sub_c20(rdi_4, rsi_5, rdx_4, &var_12d0, r8_2);
    void* rax_26 = sub_1410(0xa3e6f6c3);

    if (rax_26)
    {
        void* rax_64 = sub_1360(rax_26, 0xf9d2dde2);
        void* rax_65 = sub_1360(rax_26, 0x71948ca4);

        if (rax_64 && rax_65 && rax_64())
            rax_65();
    }

    while (true)
        /* nop */
}

void sub_c20(int64_t arg1, int64_t arg2, int64_t arg3, int64_t* arg4, int64_t arg5)
{
    int64_t rdx = *arg4;
    int64_t rax;

    if (rdx)
    {
        rax = sub_17a0(arg1, arg2, rdx, arg4);
        arg5 = 0;
        *arg4 = 0;
    }

    int64_t rdx_1 = arg4[1];

    if (rdx_1)
    {
        rax = sub_17a0(arg1, arg2, rdx_1, arg4, arg5);
        arg4[1] = 0;
    }

    int64_t rdx_2 = arg4[2];

    if (rdx_2)
    {
        rax = sub_17a0(arg1, arg2, rdx_2, arg4);
        arg4[2] = 0;
    }

    int64_t rdx_3 = arg4[3];

    if (rdx_3)
    {
        sub_17a0(arg1, arg2, rdx_3, arg4);
        arg4[3] = 0;
    }
}

int64_t __convention("win64") sub_c90(char* arg1, char* arg2)
{
    int64_t i = 0;
    int64_t var_18 = 0x7f51121412b2ccaa;
    int64_t var_10 = 0x26f31b88d7459a3e;

    do
    {
        arg2[i] = arg1[i] ^ *(&var_18 + i);
        i += 1;
    } while (i != 0xc);  /* "TUWVS" */

    return i;
}

int64_t __convention("win64") sub_cd0(char* arg1, char* arg2)
{
    int64_t i = 0;
    int64_t var_18 = 0x7f51121412b2ccaa;
    int64_t var_10 = 0x26f31b88d7459a3e;

    do
    {
        arg2[i] = arg1[i] ^ *(&var_18 + i);
        i += 1;
    } while (i != 0xd);  /* "UWVS" */

    return i;
}

int64_t __convention("win64") sub_d10(char* arg1, char* arg2)
{
    int64_t i = 0;
    int64_t var_18 = 0x7f51121412b2ccaa;
    int64_t var_10 = 0x26f31b88d7459a3e;

    do
    {
        arg2[i] = arg1[i] ^ *(&var_18 + i);
        i += 1;
    } while (i != 0xa);  /* "UATUWVS" */

    return i;
}

int64_t __convention("win64") sub_d50(char* arg1, char* arg2)
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

int64_t __convention("win64") sub_d90(int64_t* arg1)
{
    arg1[6] = sub_1410(0xa3e6f6c3);
    int64_t rax_1 = sub_1410(0xa62a3b3b);
    void* rcx = arg1[6];
    arg1[5] = rax_1;

    if (rax_1 && rcx)
    {
        void* rax_2 = sub_1360(rcx, 0x86fe8652);
        void* rcx_1 = arg1[5];
        arg1[0xd] = rax_2;  /* "UWVS" */
        void* rax_3 = sub_1360(rcx_1, 0xb3f819f8);
        void* rcx_2 = arg1[6];
        arg1[0xe] = rax_3;
        void* rax_4 = sub_1360(rcx_2, 0x29630f3d);
        void* rcx_3 = arg1[5];
        arg1[0xf] = rax_4;
        void* rax_5 = sub_1360(rcx_3, 0xa05ab779);
        arg1[0x10] = rax_5;

        if (arg1[0xd] && arg1[0xe] && arg1[0xf] && rax_5)  /* "UWVS" */
        {
            void* rax_6 = sub_1360(arg1[6], 0x53b2070f);

            if (rax_6)
            {
                int64_t var_146 = 0x1b7f202760d7bfdf;
                *(&var_146 + 7) = 0x45f6521b;  /* "AVAUATUWVS" */
                int64_t var_5a_1 = 0x26f31b88d7459a3e;
                int64_t var_62 = 0x7f51121412b2ccaa;

                for (int64_t i = 0; i != 0xb; i += 1)  /* "ATUWVS" */
                {
                    char var_13b[0xb];
                    char (* var_188_1)[0xb] = &var_13b;
                    var_13b[i] = *(&var_146 + i) ^ *(i + &var_62);
                }

                int32_t var_128_1 = 0xd729f65a;
                void var_124;
                void* var_190_1 = &var_124;
                int64_t var_130 = 0x512166607adca5dd;
                sub_c90(&var_130, &var_124);
                int64_t var_100 = 0x4d627b6473c4a8cb;
                *(&var_100 + 5) = -0x7744d601efb29d85;
                void var_f3;
                sub_cd0(&var_100, &var_f3);
                int64_t var_118 = 0x516321787ed7a4d9;
                int32_t var_110_1 = 0xd729f65a;
                void var_10c;
                sub_c90(&var_118, &var_10c);
                int64_t var_16e = 0x13353c2621dba8cd;
                int16_t var_166_1 = 0x9a52;
                void var_164;
                sub_d10(&var_16e, &var_164);
                int64_t var_15a = 0x13353c797fdca5dd;
                int16_t var_152_1 = 0x9a52;
                void var_150;
                sub_d10(&var_15a, &var_150);
                int64_t rax_7;
                int64_t rdi_2;
                rax_7 = rax_6();
                arg1[7] = rax_7;  /* "AVAUATUWVS" */
                int64_t rax_8;
                int64_t rdi_3;
                rax_8 = rdi_2();
                arg1[8] = rax_8;  /* "VAUATUWVS" */
                int64_t rax_9;
                int64_t rdi_4;
                rax_9 = rdi_3();
                arg1[9] = rax_9;  /* "AUATUWVS" */
                int64_t rax_10;
                int64_t rdi_5;
                rax_10 = rdi_4();
                arg1[0xa] = rax_10;  /* "UATUWVS" */
                int64_t rax_11;
                int64_t rdi_6;
                rax_11 = rdi_5();
                arg1[0xb] = rax_11;  /* "ATUWVS" */
                int64_t rax_12;
                int64_t rsi_1;
                int64_t rdi_7;
                rax_12 = rdi_6();
                arg1[0xc] = rax_12;  /* "TUWVS" */
                int64_t rax_13;
                int64_t rsi_2;
                int64_t rdi_8;
                rax_13 = sub_1740(rdi_7, rsi_1, 0x200, arg1);
                *arg1 = rax_13;
                int64_t rax_14;
                int64_t rsi_3;
                int64_t rdi_9;
                rax_14 = sub_1740(rdi_8, rsi_2, 0x100, arg1);
                arg1[1] = rax_14;
                int64_t rax_15;
                int64_t rsi_4;
                int64_t rdi_10;
                rax_15 = sub_1740(rdi_9, rsi_3, 0x50, arg1);
                arg1[2] = rax_15;
                int64_t rax_16;
                int16_t* rsi_5;
                rax_16 = sub_1740(rdi_10, rsi_4, 0x80, arg1);
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

                            for (int64_t i_3 = 0; i_3 != 9; i_3 += 1)  /* "AUATUWVS" */
                            {
                                int16_t rdx_8;
                                rdx_8 = *(&var_180 + i_3);
                                rdx_8 ^= *(i_3 + &var_7c);
                                var_177[i_3] = rdx_8;
                            }

                            int128_t var_8e;
                            int64_t i_4;

                            for (i_4 = 0; i_4 != 9; i_4 += 1)  /* "AUATUWVS" */
                                *(&var_8e + (i_4 << 1)) = var_177[i_4];

                            int16_t var_7e;
                            i_4 = var_7e;
                            int128_t zmm0_1 = var_8e;
                            rcx_14[1] = i_4;
                            int64_t var_e6 = 0xb3f777353f498e9;
                            *rcx_14 = zmm0_1;
                            *(&var_e6 + 5) = -0x77189454eef4c089;
                            char var_d9[0xd];
                            sub_cd0(&var_e6, &var_d9);

                            for (int64_t i_5 = 0; i_5 != 0xd; i_5 += 1)  /* "UWVS" */
                            {
                                char (* rdx_9)[0xd];
                                rdx_9 = var_d9[i_5];
                                *(&var_7c + (i_5 << 1)) = rdx_9;
                            }

                            int128_t zmm1_1 = var_7c;
                            int64_t var_cc = 0x1b3e71787ed7a4d9;
                            *rdi_11 = zmm1_1;
                            *(rdi_11 + 0xa) = *(&var_74_1 + 2);  /* "UATUWVS" */
                            *(&var_cc + 6) = 0x1be6be27b45b1b3e;
                            char var_be[0xe];
                            sub_d50(&var_cc, &var_be);

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

int64_t sub_1280()
{
    void* gsbase;
    return *(gsbase + 0x30);
}

void* sub_1290()
{
    void* gsbase;
    void* result = *(gsbase + 0x30);

    if (!result)
        return result;

    return *(result + 0x60);
}

int64_t __convention("win64") sub_12b0(int64_t arg1, int64_t arg2, char* arg3)
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

uint64_t __convention("win64") sub_12e0(char* arg1, int32_t arg2)
{
    int64_t i = 0;
    int32_t rax = -1;

    for (; i < arg2; i += 1)
    {
        int32_t r11;
        r11 = arg1[i];
        int64_t j_1 = 8;  /* "VAUATUWVS" */
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

int64_t __convention("win64") sub_1330(char* arg1, int32_t arg2)
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

void* __convention("win64") sub_1360(void* arg1, int32_t arg2)
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

            if (sub_1330(r14_1 + arg1, sub_14e0(r14_1 + arg1)) == arg2)
                return *(rdi_1 + arg1 + (*(rbp_1 + arg1 + (i << 1)) << 2)) + arg1;

            r12_2 = &r12_2[1];
        }
    }

    return sub_0;
}

int64_t __convention("win64") sub_1410(int32_t arg1)
{
    char var_428[0x400];
    __builtin_memset(&var_428, 0, 0x400);
    void* rax = sub_1290();

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

                int64_t rcx = rbx_1[0xa];  /* "UATUWVS" */

                if (rcx)
                {
                    int16_t r11_1 = rbx_1[9];  /* "AUATUWVS" */

                    if (r11_1)
                    {
                        r11_1 u>>= 1;
                        uint64_t rdx_1 = r11_1;

                        if (rdx_1 - 1 <= 0x3fe)
                        {
                            sub_12b0(rcx, rdx_1, &var_428);

                            if (sub_1330(&var_428, r11_1) == arg1)
                            {
                                int64_t result = rbx_1[4];
                                sub_16c0(&var_428, 0x400);
                                return result;
                            }

                            sub_16c0(&var_428, 0x400);
                        }
                    }
                }

                rbx_1 = *rbx_1;
            }
        }
    }

    return 0;
}

void* __convention("win64") sub_14e0(char* arg1)
{
    char* rax = arg1;

    while (*rax)
        rax = &rax[1];

    return rax - arg1;
}

int64_t __convention("win64") sub_1500(int64_t arg1)
{
    int64_t result = 0;

    if (!arg1)
        return 0;

    while (*(arg1 + (result << 1)))
        result += 1;

    return result;
}

int64_t __convention("win64") sub_1520(char* arg1)
{
    int32_t result = 0;

    while (true)
    {
        int32_t rdx_1 = *arg1;

        if (rdx_1 - 0x30 > 9)  /* "AUATUWVS" */
            break;

        arg1 = &arg1[1];
        result = result * 0xa + rdx_1 - 0x30;  /* "UATUWVS" */
    }

    return result;
}

char* __convention("win64") sub_1540(char* arg1, char* arg2)
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

uint64_t __convention("win64") sub_1570(char* arg1, int64_t arg2, char* arg3, int64_t arg4)
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

int64_t __convention("win64") sub_15f0(char* arg1, int64_t arg2, char* arg3, int64_t arg4)
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

char* __convention("win64") sub_1630(int32_t arg1, char* arg2, int32_t arg3)
{
    if (arg3 - 2 > 0x22)
    {
        *arg2 = 0;
        return arg2;
    }

    int32_t rax_1 = arg1;
    int32_t rdx;
    rdx = arg3 == 0xa;  /* "UATUWVS" */
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

        if (temp1_1 <= 9)  /* "AUATUWVS" */
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

char* __convention("win64") sub_16c0(char* arg1, int64_t arg2)
{
    for (int64_t i = 0; arg2 != i; i += 1)
        arg1[i] = 0;

    return arg1;
}

uint64_t __convention("win64") sub_16e0(void* arg1, void* arg2, int64_t arg3)
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

int64_t __convention("win64") sub_1710(char* arg1, char* arg2, int64_t arg3)
{
    int64_t i;

    for (i = 0; i != arg3; i += 1)
        arg1[i] = arg2[i] ^ *(&data_1719 + (i & 7));  /* "AVAUATUWVS" */

    return i;
}

int64_t sub_1740(int64_t arg1, int64_t arg2, int64_t arg3, void* arg4)
{
    int64_t rbx = *(arg4 + 0x70);
    int64_t rax;
    int64_t rsi_1;
    rax = (*(arg4 + 0x68))(arg1, arg3);
    /* jump -> rbx */
}

int64_t __convention("win64") sub_1770(void* arg1, int64_t arg2, int64_t arg3)
{
    int64_t rbx = *(arg1 + 0x80);
    int64_t rax;
    int64_t rsi_1;
    int64_t rdi_1;
    rax = (*(arg1 + 0x68))(arg3, arg2);
    /* jump -> rbx */
}

int64_t sub_17a0(int64_t arg1, int64_t arg2, int64_t arg3, void* arg4)
{
    int64_t rbx = *(arg4 + 0x78);
    int64_t rax;
    int64_t rsi_1;
    rax = (*(arg4 + 0x68))(arg1, arg3);
    /* jump -> rbx */
}

int64_t __convention("win64") sub_1b60(void* arg1, void* arg2, void* arg3)
{
    void* r15 = arg2;
    void* rbx = arg3 + r15;
    void* rax = sub_1360(*(arg1 + 0x30), 0x27c5f681);
    void* rax_1 = sub_1360(*(arg1 + 0x30), 0xee9d4374);
    void* rax_2 = sub_1360(*(arg1 + 0x30), 0xebcdfe95);
    char result = rax_2(sub_1360(*(arg1 + 0x30), 0x2fa62ca8), rax_1);
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

int64_t (*)() __convention("win64") sub_1c20(void* arg1, void* arg2, int64_t arg3, int32_t arg4)
{
    int64_t rbp = 0;
    int64_t rbx = arg3;
    void* rsi_1;

    while (true)
    {
        if (rbp >= *(*(arg1 + 0x3c) + arg1 + 0x50) - rbx)
            return sub_0;

        rsi_1 = arg1 + rbp;

        if (!sub_16e0(rsi_1, arg2, rbx))
            break;

        rbp += 1;
    }

    if (arg4)
        rbx = 0;

    return rsi_1 + rbx;
}

void* __convention("win64") sub_1c90(void* arg1)
{
    void* result = sub_1360(*(arg1 + 0x30), 0x71948ca4);

    if (!result)
        return result;

    /* jump -> result */
}

int64_t sub_1cc0() __pure
{
    return;
}

int64_t sub_1cd0() __pure
{
    return;
}

