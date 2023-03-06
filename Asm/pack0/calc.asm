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

.macro beq_check %rcheck, %ruse, %value, %mark
  li %rx, %value
  beq %rc, %rx, %mark
.end_macro

.macro read_operand %rd
  read_char
  
.end_macro
  
.macro _check_hex_letters

.end_macro

.macro _check_hex_decimals

.end_macro
  
.macro check_hex_digit %rcheck, %ruse,  %mark_if_failed
	li %ruse, 'f'
	bgt %rcheck, %ruse, %mark_if_failed
	
	
	
.end_macro
  

main:



	main_exit:
		exit 0
  

repl:
	repl_read_oper1:
		read_char
		li t0, 'f'
		bgt a0, t0, repl
		li t0, 'a'
		bge a0, t0, repl_read_oper1_letter
		
		repl_read_oper1_digit:
		
		repl_read_oper1_letter:
		
		
	
	
