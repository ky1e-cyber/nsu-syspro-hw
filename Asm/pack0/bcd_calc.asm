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
	li %ru, '0'
	blt %rx, %ru, %label_fail
	li %ru, '9'
	bgt %xu, %ru, %label_fail
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
		
	
	sum_branch:
		add t1, t2, t1
	
	.eqv DIGIT_WINDOW_MAX 0x0f000000
	## Digit window
	li s1, 0xf
	
	## current offset of digit position 
	li s2, 0
	bcd_normalize_begin:
		beq s1, DIGIT_WINDOW_MAX, bcd_normalize_end
		
		and t0, t1, s1
		
		j bcd_normalize_begin
	bcd_normalize_end:
	
repl_end:

exit_branch;
	exit 0
