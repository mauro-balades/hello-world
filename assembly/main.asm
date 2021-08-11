
global _start

section .text:

_start:
    mov eax, 0x4         ; use write syscall
    mov ebx, 1           ; use stdout as the fd
    mov ecx, hello       ; use the message as the buffer
    mov edx, helloLen    ; and supply the length
    int 0x80             ; invoke the syscall

    ; now exit

    mov eax, 0x1
    mov ebx, 0
    int 0x80

section .data:
	hello:     db 'hello, world',0xA    ; 'Hello world!' plus a new line
	helloLen:  equ $-hello             ; Length of the 'Hello world' string
