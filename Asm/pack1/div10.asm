.macro exit_with %rx
	li a7, 93
	mv a0, %rx
	ecall
.end_macro

.macro print_char
  li a7, 11
  ecall
.end_macro

.macro read_char
  li a7, 12
  ecall
.end_macro

.macro push_word %rx
	sw %rx, 0x0(sp)
	addi sp, sp, -4
.end_macro

.macro pop_word %rd
	addi sp, sp, 4
	lw %rd, 0x0(sp)
.end_macro

.text

call 		read_decimal
call 		div10

exit_with 	a0


# mult(a, b) = a * b
# args: a0 -- a
# 		a1 -- b
# res: 	a0 -- a*b
mult:
	li t0, 0
	mult_loop:
		andi 	t1, a1, 1
		beqz 	t1, mult_nonset
		add 	t0, t0, a0
		
	mult_nonset:
		slli a0, a0, 1
		srli a1, a1, 1
		bnez a0, mult_loop
		
	mv a0, t0
	ret


# div10(a) = 	a // 10
# args: a0 -- a
# res:	a0 -- a // 10
div10:
  li 	t0, 10
  bge 	a0, t0, div10_more_branch

  li 	a0, 0
  j 	div10_end 
  div10_more_branch:
    push_word 	ra
    
    srai		a0, a0, 2
    push_word 	a0
    call 		div10
    
    pop_word 	t0
    srai 		t0, t0, 1
    sub 		a0, t0, a0
    
    pop_word 	ra
    
  div10_end:
    ret


# read_decimal() = int(input(), base = 10)
# args: -
# res: 	a0 -- int(input(), base = 10)
read_decimal:
	push_word 	ra
	push_word 	s1
	push_word	s2
	li 			s1, 0
	
	read_decimal_l:
		read_char
		
		li 		t0, '0'
		blt 	a0, t0, read_decimal_end
		li 		t0, '9'
		bgt		a0, t0, read_decimal_end
		addi 	a0, a0, -48
		
		mv 		s2, a0
		
		mv 		a0, s1
		li 		a1, 10
		call 	mult
			
		add 	s1, s2, a0

		j 		read_decimal_l
	
	read_decimal_end:
	mv 			a0, s1
	pop_word 	s2
	pop_word 	s1
	pop_word 	ra 
	ret
