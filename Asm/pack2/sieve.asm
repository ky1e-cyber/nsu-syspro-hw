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
	sw %rx, 0x0(sp)
	addi sp, sp, -4
.end_macro

.macro pop_word %rd
	addi sp, sp, 4
	lw %rd, 0x0(sp)
.end_macro

.text


## erat_sieve(n) = ()
## prints out all prime numbers <= n to stdout
## args: a0 -- high bound of sieve
## res: ()
erat_sieve:
	push_word fp
	push_word s1
	push_word s2
	mv fp, sp
	mv s1, a0

	call calc_aligned
	sub s1 
	
	add sp sp a0
	
	
	pop_word s2
	pop_word s1
	pop_word fp
	ret
	
	
## calc_alligned(x) = (x + e), 
## where x + e is word aligned size
## args: a0 -- x
## res:	 a0 -- x + e
calc_aligned:
	## let c: u32 = 2
	## if !(x & 0x1) {
	## 		c--;
	##		if !(x & 0x10) c--;
	## }
	## return x << c;

	li 		t0, 0x2 ## counter
	
	andi 	t1, a0, 0x1
	bgtz 	t1, calc_aligned_end
	addi 	t0, -0x1
	andi 	t1, a0, 0x10
	bgtz 	t1, calc_aligned_end
	addi 	t0, -0x1

	calc_aligned_end:
	slli 	a0, a0, t0
	ret
	
	

