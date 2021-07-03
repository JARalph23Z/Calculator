import unittest
from calculator import Calculate

class Test(unittest.TestCase):
	def test__OO__sum(self):
		Solve = "1+2+3+4+5+6"
		self.assertEqual(Calculate(Solve), 21)

	def test__OO__minus(self):
		Solve = "50-10-15-5"
		self.assertEqual(Calculate(Solve), 20)

	def test__OO__multiply(self):
		Solve = "5*5*4"
		self.assertEqual(Calculate(Solve), 100)

	def test__OO__divide(self):
		Solve = "100/2/5/2"
		self.assertEqual(Calculate(Solve), 5)

	def test__OO__sum_and_minus(self):
		Solve = "2+3-2+3+3+4-10"
		self.assertEqual(Calculate(Solve), 3)

	def test__OO__multiply_and_divide(self):
		Solve = "5*5*4/10*2"
		self.assertEqual(Calculate(Solve), 20)

	def test__OO__sum_and_multiply(self):
		Solve = "1+2+3+4+5+6*2+1+2+3*4"
		self.assertEqual(Calculate(Solve), 42)

	def test__OO__combined_1(self):
		Solve = "5*3+5-2/2+14/7*3"
		self.assertEqual(Calculate(Solve), 25)

	def test__OO__combined_2(self):
		Solve = "1+9/3+1*5-100/5"
		self.assertEqual(Calculate(Solve), -11)

	def test__OO__error_division(self):
		Solve = "1+2+3+4+5+6/0"
		self.assertEqual(Calculate(Solve), "ERROR")

	def test__OO__combined_3(self):
		Solve = "(5*3)/5*9+100"
		self.assertEqual(Calculate(Solve), 127)

	def test__OO__fraction(Self):
		Solve = "(3/5)*(5/3)"
		self.assertEqual(Calculate(Solve), 1.0)

	def test__OO__addition_of_two_negative_numbers(self):
		Solve = "(-2)+(-2)"
		self.assertEqual(Calculate(Solve), -4)
	
	def test__OO__addition_of_one_positive_and_one_negative_number(self):
		Solve = "(1)+(-2)"
		self.assertEqual(Calculate(Solve), -1)

	def test__OO__subtraction_of_two_negative_numbers(self):
		Solve = "(-6)-(-2)"
		self.assertEqual(Calculate(Solve), -4)

	def test__OO__subtraction_of_one_negative_and_one_positive_number(self):
		Solve = "(-6)-(2)"
		self.assertEqual(Calculate(Solve), -8)

	def test__OO__multiplication_of_two_negative_numbers(self):
		Solve = "(-6)*(-2)"
		self.assertEqual(Calculate(Solve), 12)

	def test__OO__multiplication_of_one_negative_and_one_positive_number(self):
		Solve = "(-6)*(2)"
		self.assertEqual(Calculate(Solve), -12)

	def test__OO__division_of_two_negative_numbers(self):
		Solve = "(-6)/(-2)"
		self.assertEqual(Calculate(Solve), 3)

	def test__OO__division_of_one_negative_and_one_positive_number(self):
		Solve = "(-6)/(2)"
		self.assertEqual(Calculate(Solve), -3)

	def test__OO__multiplication_before_addition(self):
		Solve = "3+6*2"
		self.assertEqual(Calculate(Solve), 15)

	def test__OO__parentheses_first(self):
		Solve = "(3+6)*2"
		self.assertEqual(Calculate(Solve), 18)
	
	def test__OO__multiplication_and_division(self):
		Solve = "12/6*3/2"
		self.assertEqual(Calculate(Solve), 3)

	def test__OO__exponents_of_exponents(self):
		Solve = "4^3^2"
		self.assertEqual(Calculate(Solve), 262144)

	def test__OO__pemdas(self):
		Solve = "7+(6*5^2+3)"
		self.assertEqual(Calculate(Solve), 160)

	def test__OO__sin(self):
		Solve = "sin(90)"
		self.assertEqual(Calculate(Solve), 0.8939966636)

	def test__OO__cos(self):
		Solve = "cos(90)"
		self.assertEqual(Calculate(Solve), -0.44807361612)

	def test__OO__tan(self):
		Solve = "tan(45)"
		self.assertEqual(Calculate(Solve), 1.61977519054)

	def test__OO__asin(self):
		Solve = "asin(1)"
		self.assertEqual(Calculate(Solve), 1.57079632679)

	def test__OO__acos(self):
		Solve = "acos(1)"
		self.assertEqual(Calculate(Solve), 0)

	def test__OO__atan(self):
		Solve = "atan(1)"
		self.assertEqual(Calculate(Solve), 0.78539816339)
	
	def test__OO__sinh(self):
		Solve = "sinh(90)"
		self.assertEqual(Calculate(Solve), 6.102016471589175e+38)

	def test__OO__cosh(self):
		Solve = "cosh(90)"
		self.assertEqual(Calculate(Solve), 6.102016471589175e+38)

	def test__OO__tanh(self):
		Solve = "tanh(45)"
		self.assertEqual(Calculate(Solve), 1)

	def test__OO__mod(self):
		Solve = "mod(30,8)"
		self.assertEqual(Calculate(Solve), 6)
	
	def test__OO__sqrt(self):
		Solve = "sqrt(4)"
		self.assertEqual(Calculate(Solve), 2)

	def test__OO__root(self):
		Solve = "root(27,3)"
		self.assertEqual(Calculate(Solve), 3)

	def test__OO__factorial(self):
		Solve = "fact(3)"
		self.assertEqual(Calculate(Solve), 6)

	def test__OO__log(self):
		Solve = "logx(100,10)"
		self.assertEqual(Calculate(Solve), 2)

	def test__OO__log10(self):
		Solve = "log10(100)"
		self.assertEqual(Calculate(Solve), 2)

	def test__OO__log10(self):
		Solve = "ln(2)"
		self.assertEqual(Calculate(Solve), 0.6931471806)
	
	def test__OO__abs(self):
		Solve = "abs(-2)"
		self.assertEqual(Calculate(Solve), 2)

	def test__OO__abs1(self):
		Solve = "abs(-2)"
		self.assertEqual(Calculate(Solve), 2)

	def test__OO__abs2(self):
		Solve = "abs(5*(-2))"
		self.assertEqual(Calculate(Solve), 10)

	def test__OO__int1(self):
		Solve = "tnc(24.99)"
		self.assertEqual(Calculate(Solve), 24)

	def test__OO__int2(self):
		Solve = "tnc(5*2.5)"
		self.assertEqual(Calculate(Solve), 12)

	def test__OO__round1(self):
		Solve = "rnd(25.99)"
		self.assertEqual(Calculate(Solve), 26)

	def test__OO__round1(self):
		Solve = "rnd(5*2.5)"
		self.assertEqual(Calculate(Solve), 13)

	def test__OO__permutation(self):
		Solve = "P(5,2)"
		self.assertEqual(Calculate(Solve), 20)

	def test__OO__combination(self):
		Solve = "C(5,2)"
		self.assertEqual(Calculate(Solve), 10)

if __name__ == "__main__":
	unittest.main()
