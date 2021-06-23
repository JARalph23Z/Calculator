''' Ralph

Sugod sa guro ta sa basic na operations (add, minus, times, divide, dot)
Naisip nako, duha ka Class gamiton nato. First na class for the operations, then second na class para sa actual na calculator.
So dapat wala gamatter kung unsa pa na kataas ang itype sa user, dapat maunderstand niya.
Kung makaya nimo, basi maimplement na nimo ang parentheses.
Wag mo kalimutan i handle ang errors ha, 

ALSO: you might want to take a look sa numpy or math modules. murag way siya para mapadali tanan ang calculations. research mo lng.

End '''
 
class Operations:

	def __init__(self):
		pass

	def add(self, args):
		pass

	def subtract(self, args):
		pass

	def multiply(self, args):
		pass

	def divide(self, args):
		# division by 0 = error
		pass


class Calculator:
		
	def __init__(self):
		# basically diri guro i handle ang PEMDAS
		pass
		

	def calculate(self, o: Operations):
		# kunware 1 + 2 - 3 + 4, dapat mag go through the class Operations siya via 1 + 2 = 3, then 3 - 3 = 0, then 0 + 4 = 4.
		# if makaya mo, kung may parentheses like 1 + 4 * 3 * (4 + 1), dapat 4 + 1 = 5, then 4 * 3 = 12, then 12 * 5 = 60, then 1 + 60 = 61.
		
		return