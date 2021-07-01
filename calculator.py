import math
import operator
from pyparsing import *

exprStack = []

def push_first(toks):
	exprStack.append(toks[0])

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
	"sin": math.sin,
	"cos": math.cos,
	"tan": math.tan,
	"exp": math.exp,
	"asin": math.asin,
	"acos": math.acos,
	"atan": math.atan,
	"sinh": math.sinh,
	"cosh": math.cosh,
	"tanh": math.tanh,
	"mod": math.fmod,
	"sqrt": math.sqrt,
	"root": lambda a, b: a ** (1/(b)),
	"fact": math.factorial,
	"logx": math.log,
	"log10": math.log10,
	"ln": math.log,
	"abs": abs,
	"tnc": int,
	"rnd": round,
	"sgn": lambda a: -1 if a < -epsilon else 1 if a > epsilon else 0,
	"multiply": lambda a, b: a * b,
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
		return math.pi
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