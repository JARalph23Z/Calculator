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

if __name__ == "__main__":
	unittest.main()