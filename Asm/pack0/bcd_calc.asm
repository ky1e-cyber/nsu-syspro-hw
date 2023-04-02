.eqv BCD_NINES 0x99999999

.macro exit %ecode
  li a7, 93
  li a0, %ecode
  ecall
.end_macro

.macro read_char
  li a7, 12
  ecall
.end_macro

.macro read_char_to %rd
  read_char
  mv %rd, a0
.end_macro

.macro print_char
  li a7, 11
  ecall
.end_macro

.macro print_char_from %rs
  mv a0, %rs
  print_char
.end_macro

.macro check_if_digit %rx, %ru, %label_fail
	li 	%ru, '0'
	blt %rx, %ru, %label_fail
	li 	%ru, '9'
	bgt %rx, %ru, %label_fail
.end_macro

repl_begin:

	li a0, '\n'
	print_char
	
	process_operands_begin:
		li s1, 1
		li t1, 0
		li t2, 0
		read_operand_begin:
			read_char
			li 							t0, '\n'
			beq							a0, t0, repl_end
			check_if_digit 	a0, t0, read_operand_end
			addi 						a0, a0, -48
			slli 						t1, t1, 4
			add 						t1, t1, a0
			j 							read_operand_begin
			
		read_operand_end:
			li 		t0, ' '
			bne 	t0, a0, repl_begin
			beqz 	s1, process_operands_end
			li 		s1, 0
			mv 		t2, t1
			li 		t1, 0
			j 		read_operand_begin
	
	process_operands_end:
		
	read_operation:
		read_char
		li t0, '+'
		beq t0, a0, sum_branch
		li t0, '-'
		beq t0, a0, compute_ten_compliant
		j repl_begin
	
	## t2 - 1st operand
	## t1 - 2nd operand
	
	compute_ten_compliant:
		li t0, BCD_NINES
		sub t1, t0, t1
		addi t1, t1, 1
	
	sum_branch:
		li t3, 0		## Current offset
		li t4, 0		## Result
		li t5, 0xf	## Current mask
		sum_loop:
			li 		t0, 32
			bge 	t3, t0, sum_loop_end ## t3 >= t4
			
			and 	t0, t2, t5
			srl 	t0, t0, t3
			and 	t6, t1, t5
			srl 	t6, t6, t3
			
			add 	t0, t0, t6
			li 		t6, 10
			blt 	t0, t6, not_carry_branch
			
			## Carry:
			addi 	t3, t3, 4 		## (t3 + 4)
			li 		t6, 1
			sll 	t6, t6, t3
			add 	t2, t2, t6
			addi 	t0, t0, -10
			addi 	t3, t3, -4		## (t3)
						
			not_carry_branch:
			sll 	t0, t0, t3
			add 	t4, t4, t0
			
			slli 	t5, t5, 4
			addi 	t3, t3, 4
			j 	 	sum_loop
			
		sum_loop_end:
		
		li a0, '\n'
		print_char
		
		li t1, 0xf0000000		## Current Mask
		li t2, 28						## Current offset
		print_loop:
			blt 						t2, zero, print_loop_end

			and 						t3, t4, t1
			srl 						t3, t3, t2
			addi 						t3, t3, 48
			print_char_from t3
			
			srli 						t1, t1, 4
			addi 						t2, t2, -4
			j 							print_loop
			
		print_loop_end:
		j repl_begin

repl_end:

exit_branch:
	exit 0
