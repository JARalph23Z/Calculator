import math
import operator
from pyparsing import *

exprStack = []

def push_first(toks):
	exprStack.append(toks[0])


def comb(x,y):
	result = math.factorial(x) /  (math.factorial(x - y) * math.factorial(y))
	return int(result)

def perm(x,y):
	result = math.factorial(x) / math.factorial(x - y)
	return int(result)

def push_unary_minus(toks):
	for t in toks:
		if t == '-':
			exprStack.append("unary -")
		else:
			break

bnf = None

def BNF():
	global bnf
	if not bnf:
		e = CaselessKeyword("E")
		pi = CaselessKeyword("PI")
		fnumber = Regex(r"[+-]?\d+(?:\.\d*)?(?:[eE][+-]?\d+)?")
		ident = Word(alphas, alphanums + "_$")

		plus, minus, mult, div = map(Literal, "+-*/")
		lpar, rpar = map(Suppress, "()")
		addop = plus | minus
		multop = mult | div
		expop = Literal("^")

		expr = Forward()
		expr_list = delimitedList(Group(expr))

		def insert_fn_argcount_tuple(t):
			fn = t.pop(0)
			num_args = len(t[0])
			t.insert(0, (fn, num_args))

		fn_call = (ident + lpar - Group(expr_list) + rpar).setParseAction(insert_fn_argcount_tuple)
		atom = (
			addop[...]
			+ (
				(fn_call | pi | e | fnumber | ident).setParseAction(push_first)
				| Group(lpar + expr + rpar)
			)
		).setParseAction(push_unary_minus)

		factor = Forward()
		factor <<= atom + (expop + factor).setParseAction(push_first)[...]
		term = factor + (multop + factor).setParseAction(push_first)[...]
		expr <<= term + (addop + term).setParseAction(push_first)[...]
		bnf = expr

	return bnf

epsilon = 1e-12

opn = {
	"+": operator.add,
	"-": operator.sub,
	"*": operator.mul,
	"/": operator.truediv,
	"^": operator.pow,
}

fn = {
	"sin": math.sin, # sin(60)
	"cos": math.cos,
	"tan": math.tan,
	"exp": math.exp, # skip
	"asin": math.asin, # sin(between -1 and 1 lang ang values)
	"acos": math.acos, 
	"atan": math.atan,
	"sinh": math.sinh, # sinh(60)
	"cosh": math.cosh,
	"tanh": math.tanh,
	"mod": math.fmod, # mod(30, 8) = 6, mod(10, 3) = 1
	"sqrt": math.sqrt, # sqrt(4) = 2
	"root": lambda a, b: a ** (1/(b)), # root(27, 3) = 3, root(125, 3) = 5, root(625, 4) = 5
	"fact": math.factorial, # fact(3) = 3*2*1 = 6
	"logx": math.log, # log(100, 10) = 2
	"log10": math.log10, # log(100, 10) = 2
	"ln": math.log, # ln(2)
	"P": perm,
	"C": comb,
	"abs": abs, # abs(-1) = 1, abs(10 * (-2)) = 20
	"tnc": int, # tnc(25.92) = 25, tnc(5 * 2.1) = 10
	"rnd": round, # rnd(25.92) = 26 , rnd(25.92, 1) = 25.9, rnd(25.945, 2) = 25.95
	"sgn": lambda a: -1 if a < -epsilon else 1 if a > epsilon else 0, # skip
	"multiply": lambda a, b: a * b, # skip
	}


def evaluate_stacks(s):
	op, num_args = s.pop(), 0
	if isinstance(op, tuple):
		op, num_args = op
	if op == "unary -":
		return -evaluate_stacks(s)
	if op in "+-*/^":
		try:
			op2 = evaluate_stacks(s)
			op1 = evaluate_stacks(s)
			return opn[op](op1, op2)
		except:
			return "ERROR"
	elif op == "PI":
		return round(math.pi, 2)
	elif op == "E":
		return math.e
	elif op in fn:
		try:
			args = reversed([evaluate_stacks(s) for _ in range(num_args)])
			return fn[op](*args)
		except ValueError:
			return "An error occured, please make sure you follow the guidelines."
	elif op[0].isalpha():
		raise Exception("Invalid Identifier '%s'" % op)
	else:
		try:
			return int(op)
		except ValueError:
			return float(op)

def Calculate(s):
	
	try:
		exprStack[:] = []
		results = BNF().parseString(s, parseAll = True)
		val = evaluate_stacks(exprStack[:])
		return val

	except:
		return 'ERROR'

print(Calculate('C(10,3)'))