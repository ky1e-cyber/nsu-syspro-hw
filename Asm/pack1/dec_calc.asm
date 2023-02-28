.macro exit %ecode
  li a7, 93
  li a0, %ecode
  ecall
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
	mv t0, ra
	
	
	
	mv ra, t0
	ret


