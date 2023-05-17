.macro exit %ecode
  li a7, 93
  li a0, %ecode
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

.macro print_char_from %rs
  mv a0, %rs
  print_char
.end_macro

.macro push_word %rx
	addi sp, sp, -4
	sw %rx, 0x0(sp)
	
.end_macro

.macro pop_word %rd
	lw %rd, 0x0(sp)
	addi sp, sp, 4
.end_macro

.text
repl:
	repl_l:
		li 			a0, '\n'
		print_char
		
		call 		read_decimal
		mv 			s1, a0
		call 		read_decimal
		mv 			s2, a0
		
		read_char
		
		li 			t0, '+'
		beq 		a0, t0, repl_branch_sum
		
		li 			t0, '-'
		beq 		a0, t0, repl_branch_sub
		
		li 			t0, '*'
		beq 		a0, t0, repl_branch_mult
		
		j 			repl_l_end
		
		repl_branch_sum:
			add a0, s1, s2
			j 	repl_print
		
		repl_branch_sub:
			sub a0, s1, s2
			j 	repl_print
		
		repl_branch_mult:
			mv 		a0, s1
			mv 		a1, s2
			call 	mult
			j 		repl_print
			
		repl_print:
			mv 			s1, a0
			li 			a0, '\n'
			print_char
			mv 			a0, s1
			call 		print_decimal
		
		repl_l_end:
			li 				t0, '\n'
			print_char_from t0
			read_char
			beq 			a0, t0, repl_l

repl_end:
	exit 0


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
	div a0, a0, t0
	ret


# mod10(a) = a - 10 * (a // 10)
# args: a0 -- a
# res:	a0 -- a mod 10 
mod10:
	push_word 	ra
	push_word 	a0
	
	call 		div10
	
	li 			a1, 10
	call 		mult

	pop_word 	t0
	sub			a0, t0, a0
	pop_word 	ra
	
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


.macro push_last_digit %rx
	mv 			a0, %rx
	call 		mod10
	push_word 	a0
.end_macro

.macro rem_last_digit %rx
	mv 		a0, %rx
	call 	div10
	mv 		%rx, a0
.end_macro

# print_decimal(a) = print(a) = ()
# args: a0 -- a
# res: -
print_decimal:
	push_word		ra
	push_word 		s1
	push_word 		s2
	
	mv 				s1, a0
	call 			mod10
	push_word 		a0
	
	rem_last_digit 	s1
	
	li 				s2, 1 # counter
	
	print_decimal_fill:
		beq 				s1, zero, print_decimal_l
		addi 				s2, s2, 1
		push_last_digit 	s1
		rem_last_digit 		s1
		j 					print_decimal_fill
	
	print_decimal_l:
		beq 				s2, zero, print_decimal_end
		addi 				s2, s2, -1
		pop_word 			a0
		addi 				a0, a0, 48
		print_char
		j 					print_decimal_l
	
	print_decimal_end:
		pop_word s2
		pop_word s1
		pop_word ra
	ret
	
