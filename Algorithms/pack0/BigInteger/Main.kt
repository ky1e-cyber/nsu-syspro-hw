import java.math.BigInteger

fun longDivision(_dividend: BigInteger, divisor: BigInteger): BigInteger {

	if (divisor == BigInteger.ZERO) throw ArithmeticException()

	var dividend = _dividend
	var quotient = BigInteger.ZERO

	while (dividend > divisor) {

		var multiplier = 1.toBigInteger()

		while (dividend >= multiplier * divisor) {
			multiplier = (multiplier shl 1)
		}

		multiplier = multiplier shr 1
		quotient += multiplier
		dividend -= multiplier * divisor
	}

	return quotient
}

fun karatsubaMul(x: BigInteger, y: BigInteger): BigInteger {

	val len = maxOf(x.bitLength(), y.bitLength())

	if (len <= 2) 
		return x * y

	val halfLen = (len / 2) + (len % 2)

	val (x_l, y_l) = arrayOf(x, y).map{ it shr halfLen }
	
	val x_r = x - (x_l shl halfLen)
	val y_r = y - (y_l shl halfLen)

	val p_1 = karatsubaMul(x_l, y_l)
	val p_2 = karatsubaMul(x_r, y_r)
	val p_3 = karatsubaMul(x_l + x_r, y_l + y_r)

	return (
		(p_1 shl (2 * halfLen))
		+ p_2
		+ ((p_3 - p_2 - p_1) shl halfLen)
	)	
} 

fun main(argv: Array<String>) {

	if (argv.size != 2) throw IllegalArgumentException()



	val (operand1, operand2) = argv.map{ it.toBigInteger() }

	print("${longDivision(operand1, operand2)} ${karatsubaMul(operand1, operand2)}")
}
