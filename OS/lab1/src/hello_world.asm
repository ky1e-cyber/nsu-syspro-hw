[BITS 16]

cli
mov ax, 0x7c0
mov ds, ax
sti

mov al, [hello_str + bx]

hello_str:
    db 'Hello, BIOS', 0

times (510 - ($ - $$)) db 0
dw 0xAA55