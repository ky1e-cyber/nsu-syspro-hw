.macro exit %ecode
  li a7, 93
  li a0, %ecode
  ecall
.end_macro

.macro print_char
  li a7, 11
  ecall
.end_macro

.macro read_char_to %rd
  read_char
  mv %rd, a0
.end_macro

.macro read_char
  li a7, 12
  ecall
.end_macro

read_char_to 	t1

li 						a0, '\n'
print_char

li 						t0, '0'
blt 					t1, t0, exit_branch
li 						t0, '9'
bgt 					t1, t0, exit_branch

li 						a0, '1'
print_char

li 						a0, '\n'
print_char

exit_branch:
	exit 0
