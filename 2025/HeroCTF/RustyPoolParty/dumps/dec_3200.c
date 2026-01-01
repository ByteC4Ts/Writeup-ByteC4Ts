int64_t sub_0()
{
    int64_t var_53;
    __builtin_strcpy(&var_53, "FLAG PART_0: Hero{y0u_700_");
    void* rax = sub_3b0(0xa3e6f6c3);

    if (rax)
    {
        void* rax_1 = sub_300(rax, 0x2fa62ca8);
        void* rax_2 = sub_300(rax, 0xe53f7a31);
        void* rax_3 = sub_300(rax, 0xbdcac9ce);
        void* rax_4 = sub_300(rax, 0x7f07c44a);
        void* rdi_1 = sub_300(rax, 0xfaba0065);

        if (rax_1 && rax_2)
        {
            void* rax_5;
            rax_5 = !rax_3;
            rax_5 |= !rax_4;

            if (!rax_5 && rdi_1)
            {
                rax_1();
                int64_t var_7b_1 = 0x26817efca424f762;
                int64_t var_5b_1 = 0x26f31b88d7459a3e;
                int64_t var_83 = 0x1a217b644e9c90f6;
                int64_t var_63 = 0x7f51121412b2ccaa;

                for (int64_t i = 0; i != 0x10; i += 1)  /* "0: HerATUWVSH" */
                {
                    char var_73[0x10];
                    var_73[i] = *(&var_83 + i) ^ *(&var_63 + i);
                }

                int32_t var_a8_1 = 3;
                int64_t var_98_1 = 0;
                int32_t var_a0_1 = 0;

                if (rax_3() != -1)
                {
                    var_a8_1 = 0;
                    var_63 = 1;
                    *(&var_63 + 1) = 0;
                    int32_t var_88 = 0;
                    rax_4()();
                    void* rax_7 = sub_3b0(0xa3e6f6c3);

                    if (rax_7)
                    {
                        void* rax_8 = sub_300(rax_7, 0xf9d2dde2);
                        void* rax_9 = sub_300(rax_7, 0x71948ca4);

                        if (rax_8 && rax_9 && rax_8())
                            rax_9();
                    }

                    while (true)
                        /* nop */
                }
            }
        }
    }

    return 1;
}

int64_t sub_220()
{
    void* gsbase;
    return *(gsbase + 0x30);
}

void* sub_230()
{
    void* gsbase;
    void* result = *(gsbase + 0x30);

    if (!result)
        return result;

    return *(result + 0x60);
}

int64_t __convention("win64") sub_250(int64_t arg1, int64_t arg2, char* arg3)
{
    int64_t i;

    for (i = 0; i != arg2; i += 1)
    {
        int32_t r9;
        r9 = *(arg1 + (i << 1));

        if (r9 - 0x41 <= 0x19)  /* "WVSH" */
            r9 += 0x20;

        arg3[i] = r9;
    }

    return i;
}

uint64_t __convention("win64") sub_280(char* arg1, int32_t arg2)
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

int64_t __convention("win64") sub_2d0(char* arg1, int32_t arg2)
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

void* __convention("win64") sub_300(void* arg1, int32_t arg2)
{
    if (!arg1)
        return 0;

    int32_t* rax_1 = *(arg1 + 0x3c) + arg1;  /* "700_" */

    if (*rax_1 == 0x4550)
    {
        int64_t i = 0;
        void* rsi_2 = rax_1[0x22] + arg1;
        uint64_t rdi_1 = *(rsi_2 + 0x1c);
        uint64_t rbp_1 = *(rsi_2 + 0x24);
        int32_t* r12_2 = *(rsi_2 + 0x20) + arg1;

        for (; i < *(rsi_2 + 0x14); i += 1)  /* "erATUWVSH" */
        {
            uint64_t r14_1 = *r12_2;

            if (sub_2d0(r14_1 + arg1, sub_480(r14_1 + arg1)) == arg2)
                return *(rdi_1 + arg1 + (*(rbp_1 + arg1 + (i << 1)) << 2)) + arg1;

            r12_2 = &r12_2[1];
        }
    }

    return sub_0;
}

int64_t __convention("win64") sub_3b0(int32_t arg1)
{
    char var_428[0x400];
    __builtin_memset(&var_428, 0, 0x400);
    void* rax = sub_230();

    if (rax)
    {
        void* rax_1 = *(rax + 0x18);  /* "UWVSH" */

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
                            sub_250(rcx, rdx_1, &var_428);

                            if (sub_2d0(&var_428, r11_1) == arg1)
                            {
                                int64_t result = rbx_1[4];
                                sub_660(&var_428, 0x400);
                                return result;
                            }

                            sub_660(&var_428, 0x400);
                        }
                    }
                }

                rbx_1 = *rbx_1;
            }
        }
    }

    return 0;
}

void* __convention("win64") sub_480(char* arg1)
{
    char* rax = arg1;

    while (*rax)
        rax = &rax[1];

    return rax - arg1;
}

int64_t __convention("win64") sub_4a0(int64_t arg1)
{
    int64_t result = 0;

    if (!arg1)
        return 0;

    while (*(arg1 + (result << 1)))
        result += 1;

    return result;
}

int64_t __convention("win64") sub_4c0(char* arg1)
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

char* __convention("win64") sub_4e0(char* arg1, char* arg2)
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

uint64_t __convention("win64") sub_510(char* arg1, int64_t arg2, char* arg3, int64_t arg4)
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

int64_t __convention("win64") sub_590(char* arg1, int64_t arg2, char* arg3, int64_t arg4)
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

char* __convention("win64") sub_5d0(int32_t arg1, char* arg2, int32_t arg3)
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

char* __convention("win64") sub_660(char* arg1, int64_t arg2)
{
    for (int64_t i = 0; arg2 != i; i += 1)
        arg1[i] = 0;

    return arg1;
}

uint64_t __convention("win64") sub_680(void* arg1, void* arg2, int64_t arg3)
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

int64_t __convention("win64") sub_6b0(char* arg1, char* arg2, int64_t arg3)
{
    int64_t i;

    for (i = 0; i != arg3; i += 1)
        arg1[i] = arg2[i] ^ *(&data_6b9 + (i & 7));

    return i;
}

int64_t sub_6e0(int64_t arg1, int64_t arg2, int64_t arg3, void* arg4)
{
    int64_t rbx = *(arg4 + 0x70);
    int64_t rax;
    int64_t rsi_1;
    rax = (*(arg4 + 0x68))(arg1, arg3);
    /* jump -> rbx */
}

int64_t __convention("win64") sub_710(void* arg1, int64_t arg2, int64_t arg3)
{
    int64_t rbx = *(arg1 + 0x80);
    int64_t rax;
    int64_t rsi_1;
    int64_t rdi_1;
    rax = (*(arg1 + 0x68))(arg3, arg2);
    /* jump -> rbx */
}

int64_t sub_740(int64_t arg1, int64_t arg2, int64_t arg3, void* arg4)
{
    int64_t rbx = *(arg4 + 0x78);
    int64_t rax;
    int64_t rsi_1;
    rax = (*(arg4 + 0x68))(arg1, arg3);
    /* jump -> rbx */
}

int64_t __convention("win64") sub_b00(void* arg1, void* arg2, void* arg3)
{
    void* r15 = arg2;
    void* rbx = arg3 + r15;
    void* rax = sub_300(*(arg1 + 0x30), 0x27c5f681);
    void* rax_1 = sub_300(*(arg1 + 0x30), 0xee9d4374);
    void* rax_2 = sub_300(*(arg1 + 0x30), 0xebcdfe95);
    char result = rax_2(sub_300(*(arg1 + 0x30), 0x2fa62ca8), rax_1);
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

int64_t (*)() __convention("win64") sub_bc0(void* arg1, void* arg2, int64_t arg3, int32_t arg4)
{
    int64_t rbp = 0;
    int64_t rbx = arg3;
    void* rsi_1;

    while (true)
    {
        if (rbp >= *(*(arg1 + 0x3c) + arg1 + 0x50) - rbx)  /* "700_" */
            return sub_0;

        rsi_1 = arg1 + rbp;

        if (!sub_680(rsi_1, arg2, rbx))
            break;

        rbp += 1;
    }

    if (arg4)
        rbx = 0;

    return rsi_1 + rbx;
}

void* __convention("win64") sub_c30(void* arg1)
{
    void* result = sub_300(*(arg1 + 0x30), 0x71948ca4);

    if (!result)
        return result;

    /* jump -> result */
}

