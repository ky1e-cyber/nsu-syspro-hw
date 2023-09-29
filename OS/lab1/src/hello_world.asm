[BITS 16]

cli
mov ax, 0x7c0
mov ds, ax
mov ss, ax
mov sp, 0x0
sti

mov bx, 0x0
mov ah, 0xe

print_loop:
    mov al, [hello_str + bx]
    test al, al
    jz endless
    int 0x10
    inc bx
    jmp print_loop

endless:
    jmp endless

hello_str:
    db `Hello, BIOS\r\n`, 0x0

times (510 - ($ - $$)) db 0x0
dw 0xAA55