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
  
 
repl:

	# read operands
		repl_read_oper1:
			read_char
			li t0, ' '
			beq t0, a0, repl_read_oper2
			
			li t0, 'f'
			bgt a0, t0, repl
			
			li t0, 'a'
			bge a0, t0, repl_read_oper1_letter
			
			li t0, '9'
			bgt a0, t0, repl
			
			li t0, '0'
			bge a0 t0, repl_read_oper1_digit
			
			j repl

			repl_read_oper1_digit:
				addi a0, a0, -48
				j repl_read_oper1_end
				
			repl_read_oper1_letter:
				addi a0, a0,  -87
				
		repl_read_oper1_end:
			slli t1, t1, 4
			add t1, t1, a0
			j repl_read_oper1
			
		repl_read_oper2:
			read_char
			li t0, ' '
			beq t0, a0, repl_read_operator
			
			li t0, 'f'
			bgt a0, t0, repl
			
			li t0, 'a'
			bge a0, t0, repl_read_oper2_letter
			
			li t0, '9'
			bgt a0, t0, repl
			
			li t0, '0'
			bge a0 t0, repl_read_oper2_digit
			
			j repl

			repl_read_oper2_digit:
				addi a0, a0, -48
				j repl_read_oper2_end
				
			repl_read_oper2_letter:
				addi a0, a0,  -87
				
		repl_read_oper2_end:
			slli t2, t2, 4
			add t2, t2, a0
			j repl_read_oper2
			
				
		repl_read_operator:	
			read_char
			li 	t0, '+'
			beq t0, a0, repl_branch_add
			li t0, '-'
			beq t0, a0, repl_branch_sub
			li t0, '&'
			beq t0, a0, repl_branch_and
			li t0, '|'
			beq t0, a0, repl_branch_or
			j repl_print_end
		
		repl_branch_add:
			add t1, t1, t2
			j repl_branches_end
		
		repl_branch_sub:
			sub t1, t1, t2
			j repl_branches_end
		
		repl_branch_and:
			and t1, t1, t2
			j repl_branches_end
		
		repl_branch_or:
			or t1, t1, t2
		
		repl_branches_end:
			li a0, '\n'
			print_char
			li t3, 32

		repl_print:
		
			blez t3, repl_print_end 
			addi t3, t3, -4
	
			srl t0, t1, t3
			sll t0, t0, t3
			sub t1, t1, t0
			srl t0, t0, t3
				
			li t2, 10
			blt t0, t2, repl_print_digit
			
			repl_print_letter:
				addi t0, t0, 87
				j repl_print_out
				
			repl_print_digit: 
				addi t0, t0, 48
				
			repl_print_out:
				print_char_from t0
			
			j repl_print
			
		repl_print_end:
			li a0, '\n'
			print_char 
			j repl_end
							
		repl_end:
			li t0, 0
			li t1, 0
			li t2, 0
			li t3, 0
			j repl
			
_exit:
	exit 0
		
		
		

		
		
	
	
