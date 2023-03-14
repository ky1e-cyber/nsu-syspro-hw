.macro exit %ecode
  li a7, 93
  li a0, %ecode
  ecall
.end_macro

.macro print_char
  li a7, 11
  ecall
.end_macro

.macro print_char_from %rs
  mv a0, %rs
  print_char
.end_macro

.macro print_newline
	li a0, '\n'
	print_char
.end_macro

.macro read_char
  li a7, 12
  ecall
.end_macro

.macro read_char_to %rd
  read_char
  mv %rd, a0
.end_macro

read_print_loop:
	read_char_to 		t1
	li 							a0, '\n'
	beq 						a0, t1, read_print_loop_end
	print_char
	
	print_char_from t1
	addi 						t1, t1, 1
	print_newline
	print_char_from t1
	print_newline
	j 							read_print_loop

read_print_loop_end:
	exit 0