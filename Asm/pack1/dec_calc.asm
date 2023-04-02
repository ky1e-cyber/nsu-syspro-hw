.macro exit %ecode
  li a7, 93
  li a0, %ecode
  ecall
.end_macro

.macro push_word %rx
	sw %rx, 0x0(sp)
	addi sp, -4
.end_macro

.macro pop_word %rd
	lw %rd, 0x0(sp)
	addi sp, 4
.end_macro

.text
main:
	li a7, 12
	ecall
	addi a1, a0, -0x30
	
	
	ecall
	addi a0, a0, -0x30
	
	call mult
	
	li a7, 11
	ecall
	
	exit 0

# mult(a, b) = a*b

# args: a0 -- a
# 			a1 -- b
# res: 	a0 -- a*b
mult:
	li t0, 0
	mult_loop:
		andi t1, a1, 1
		beqz t1, mult_nonset
		add t0, t0, a0
		
	mult_nonset:
		slli a0, a0, 1
		srli a1, a1, 1
		bnez a0, mult_loop
		
	mv a0, t0
	ret
	
	
# div10(a) = a // 10

# args: a0 -- a
# res		a0 -- a // 10
div10:
	
	li t0, 10
	ble a0, t0, div10_zero_branch
	
	push_word ra
	
	
	pop_word ra
	
	div10_zero_branch:
		li a0, 0
	
	ret


