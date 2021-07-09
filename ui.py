import sys
from functools import partial
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from threading import Thread
from playsound import playsound

import calculator

class Resizing(QStackedWidget):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.currentChanged.connect(self.updateGeometry)

	def minimumSizeHint(self):
		return self.sizeHint()
		
	def sizeHint(self):
		current = self.currentWidget()
		if not current:
			return super().sizeHint()
		return current.sizeHint()

class CalculatorUI(QMainWindow):

	def __init__(self):
		super().__init__()
		self.basic_buttons = {}
		self.sci_buttons = {}

		self.setWindowTitle('Calculator')
		self.setWindowIcon(QIcon('./resources/window_icon.png'))
		self.setFixedSize(380, 485)
		
		central_widget = QWidget()
		self.setCentralWidget(central_widget)

		self.layout = QVBoxLayout(central_widget)
		self.create_equateLine()

		self.stacked_widget = Resizing()

		self.layout.addWidget(self.stacked_widget, alignment = Qt.AlignmentFlag.AlignCenter)

		maps = [
			{
		'ANS': (0, 0, 1, 1),
		'DEL': (0, 1, 1, 1),
		'AC': (0, 2, 1, 1),
		'(': (0, 3, 1, 1),
		')': (0, 4, 1, 1),
		'7': (1, 0, 1, 1),
		'8': (1, 1, 1, 1),
		'9': (1, 2, 1, 1),
		'÷': (1, 3, 1, 1),
		f"x\N{SUPERSCRIPT TWO}": (1, 4, 1, 1),
		'4': (2, 0, 1, 1),
		'5': (2, 1, 1, 1),
		'6': (2, 2, 1, 1),
		'x': (2, 3, 1, 1),
		f'\N{SUPERSCRIPT TWO}√': (2, 4, 1, 1),
		'1': (3, 0, 1, 1),
		'2': (3, 1, 1, 1),
		'3': (3, 2, 1, 1),
		'-': (3, 3, 1, 1),
		'=': (3, 4, 2, 1),
		'0': (4, 0, 1, 2),
		'.': (4, 2, 1, 1),
		'+': (4, 3, 1, 1)
		},
		{
		'RND': (0, 0, 1, 1),
		'TNC': (0, 1, 1, 1),
		'ABS': (0, 2, 1, 1),
		'nCr': (0, 3, 1, 1),
		'nPr': (0, 4, 1, 1),
		'ANS': (0, 5, 1, 1),
		'DEL': (0, 6, 1, 1),
		'AC': (0, 7, 1, 1),
		'(': (0, 8, 1, 1),
		')': (0, 9, 1, 1),
		'xⁿ': (1, 0, 1, 1),
		'sin': (1, 1, 1, 1),
		'sinh': (1, 2, 1, 1),
		'sin⁻¹': (1, 3, 1, 1),
		'ln': (1, 4, 1, 1),
		'7': (1, 5, 1, 1),
		'8': (1, 6, 1, 1),
		'9': (1, 7, 1, 1),
		'÷': (1, 8, 1, 1),
		f"x\N{SUPERSCRIPT TWO}": (1, 9, 1, 1),
		'ʸ√x': (2, 0, 1, 1),
		'cos': (2, 1, 1, 1),
		'cosh': (2, 2, 1, 1),
		'cos⁻¹': (2, 3, 1, 1),
		'logₙx': (2, 4, 1, 1),
		'4': (2, 5, 1, 1),
		'5': (2, 6, 1, 1),
		'6': (2, 7, 1, 1),
		'x': (2, 8, 1, 1),
		f'\N{SUPERSCRIPT TWO}√': (2, 9, 1, 1),
		'π': (3, 0, 1, 1),
		'tan': (3, 1, 1, 1),
		'tanh': (3, 2, 1, 1),
		'tan⁻¹': (3, 3, 1, 1),
		'log₁₀': (3, 4, 1, 1),
		'1': (3, 5, 1, 1),
		'2': (3, 6, 1, 1),
		'3': (3, 7, 1, 1),
		'-': (3, 8, 1, 1),
		'=': (3, 9, 2, 1),
		'!': (4, 0, 1, 1),
		'eˣ': (4, 1, 1, 1),
		'mod': (4, 2, 1, 1),
		',': (4, 3, 1, 1),
		'x10ˣ': (4, 4, 1, 1),
		'0': (4, 5, 1, 2),
		'.': (4, 7, 1, 1),
		'+': (4, 8, 1, 1)
			}
		]

	
		page_1 = self.create_page_basic(maps[0])
		page_2 = self.create_page_sci(maps[1])
		self.stacked_widget.addWidget(page_1)
		self.stacked_widget.addWidget(page_2)

		self.set_ObjectName()

	def create_equateLine(self):

		self.equateLine = QLineEdit()
		self.equateLine.setFixedHeight(60)
		self.equateLine.setAlignment(Qt.AlignmentFlag.AlignRight)
		self.layout.addWidget(self.equateLine)

	def create_page_basic(self, map_letters):

		page = QWidget()
		grid_layout = QGridLayout(page)

		for btnText, pos in map_letters.items():

			if btnText in ['÷', f"x\N{SUPERSCRIPT TWO}", f'\N{SUPERSCRIPT TWO}√', 'x']:
				if btnText == '÷':
					self.basic_buttons['/'] = QPushButton(btnText)
				elif btnText == f"x\N{SUPERSCRIPT TWO}":
					self.basic_buttons['^2'] = QPushButton(btnText)
				elif btnText == f'\N{SUPERSCRIPT TWO}√':
					self.basic_buttons['sqrt('] = QPushButton(btnText)
				elif btnText == 'x':
					self.basic_buttons['*'] = QPushButton(btnText)
			else:
				self.basic_buttons[btnText] = QPushButton(btnText)

			if btnText in ['0', '=']:
				if btnText == '=':
					self.basic_buttons[btnText].setFixedSize(60, 126)
				else:
					self.basic_buttons[btnText].setFixedSize(126, 60)

				grid_layout.addWidget(self.basic_buttons[btnText], pos[0], pos[1], pos[2], pos[3])

			else:

				if btnText in ['÷', f"x\N{SUPERSCRIPT TWO}", f'\N{SUPERSCRIPT TWO}√', 'x']:

					if btnText == '÷':
						self.basic_buttons['/'].setFixedSize(60, 60)
						grid_layout.addWidget(self.basic_buttons['/'], pos[0], pos[1], pos[2], pos[3])

					elif btnText == f"x\N{SUPERSCRIPT TWO}":
						self.basic_buttons['^2'].setFixedSize(60, 60)
						grid_layout.addWidget(self.basic_buttons['^2'], pos[0], pos[1], pos[2], pos[3])

					elif btnText == f'\N{SUPERSCRIPT TWO}√':
						self.basic_buttons['sqrt('].setFixedSize(60, 60)
						grid_layout.addWidget(self.basic_buttons['sqrt('], pos[0], pos[1], pos[2], pos[3])

					elif btnText == 'x':
						self.basic_buttons['*'].setFixedSize(60, 60)
						grid_layout.addWidget(self.basic_buttons['*'], pos[0], pos[1], pos[2], pos[3])
					
				else:
					self.basic_buttons[btnText].setFixedSize(60, 60)
					grid_layout.addWidget(self.basic_buttons[btnText], pos[0], pos[1], pos[2], pos[3])

		return page

	def create_page_sci(self, map_letters):

		page = QWidget()
		grid_layout = QGridLayout(page)

		for btnText, pos in map_letters.items():

			if btnText in ['÷', f"x\N{SUPERSCRIPT TWO}", f'\N{SUPERSCRIPT TWO}√', 'x']:
				if btnText == '÷':
					self.sci_buttons['/'] = QPushButton(btnText)
				elif btnText == f"x\N{SUPERSCRIPT TWO}":
					self.sci_buttons['^2'] = QPushButton(btnText)
				elif btnText == f'\N{SUPERSCRIPT TWO}√':
					self.sci_buttons['sqrt('] = QPushButton(btnText)
				elif btnText == 'x':
					self.sci_buttons['*'] = QPushButton(btnText)
			
			elif btnText in ['RND', 'TNC', 'ABS', 'sin', 'sinh', 'cos', 'cosh', 'tan', 'tanh', 'mod', 'ln']:
				self.sci_buttons[btnText.lower() + '('] = QPushButton(btnText)

			else:
				if btnText == 'π':
					self.sci_buttons['pi'] = QPushButton(btnText)
				elif btnText == 'xⁿ':
					self.sci_buttons['^'] = QPushButton(btnText)
				elif btnText == 'sin⁻¹':
					self.sci_buttons['asin('] = QPushButton(btnText)
				elif btnText == 'cos⁻¹':
					self.sci_buttons['acos('] = QPushButton(btnText)
				elif btnText == 'tan⁻¹':
					self.sci_buttons['atan('] = QPushButton(btnText)
				elif btnText == 'ʸ√x':
					self.sci_buttons['root('] = QPushButton(btnText)
				elif btnText == 'logₙx':
					self.sci_buttons['logx('] = QPushButton(btnText)
				elif btnText == 'log₁₀':
					self.sci_buttons['log10('] = QPushButton(btnText)
				elif btnText == '!':
					self.sci_buttons['fact('] = QPushButton(btnText)
				elif btnText == 'eˣ':
					self.sci_buttons['e^'] = QPushButton(btnText)
				elif btnText == 'x10ˣ':
					self.sci_buttons['*10^'] = QPushButton(btnText)
				elif btnText == 'nCr':
					self.sci_buttons['C('] = QPushButton(btnText)
				elif btnText == 'nPr':
					self.sci_buttons['P('] = QPushButton(btnText)
				else:
					self.sci_buttons[btnText] = QPushButton(btnText)

			if btnText in ['0', '=']:
				if btnText == '=':
					self.sci_buttons[btnText].setFixedSize(60, 126)
				elif btnText == '0':
					self.sci_buttons[btnText].setFixedSize(126, 60)

				grid_layout.addWidget(self.sci_buttons[btnText], pos[0], pos[1], pos[2], pos[3])

			else:
				if btnText in ['÷', f"x\N{SUPERSCRIPT TWO}", f'\N{SUPERSCRIPT TWO}√', 'x']:

					if btnText == '÷':
						self.sci_buttons['/'].setFixedSize(60, 60)
						grid_layout.addWidget(self.sci_buttons['/'], pos[0], pos[1], pos[2], pos[3])

					elif btnText == f"x\N{SUPERSCRIPT TWO}":
						self.sci_buttons['^2'].setFixedSize(60, 60)
						grid_layout.addWidget(self.sci_buttons['^2'], pos[0], pos[1], pos[2], pos[3])

					elif btnText == f'\N{SUPERSCRIPT TWO}√':
						self.sci_buttons['sqrt('].setFixedSize(60, 60)
						grid_layout.addWidget(self.sci_buttons['sqrt('], pos[0], pos[1], pos[2], pos[3])

					elif btnText == 'x':
						self.sci_buttons['*'].setFixedSize(60, 60)
						grid_layout.addWidget(self.sci_buttons['*'], pos[0], pos[1], pos[2], pos[3])

				elif btnText in ['RND', 'TNC', 'ABS', 'sin', 'sinh', 'cos', 'cosh', 'tan', 'tanh', 'mod', 'ln']:
					self.sci_buttons[btnText.lower() + '('].setFixedSize(60, 60)
					grid_layout.addWidget(self.sci_buttons[btnText.lower() + '('], pos[0], pos[1], pos[2], pos[3])

				else:

					if btnText == 'π':
						self.sci_buttons['pi'].setFixedSize(60, 60)
						grid_layout.addWidget(self.sci_buttons['pi'], pos[0], pos[1], pos[2], pos[3])

					elif btnText == 'xⁿ':
						self.sci_buttons['^'].setFixedSize(60, 60)
						grid_layout.addWidget(self.sci_buttons['^'], pos[0], pos[1], pos[2], pos[3])

					elif btnText == 'sin⁻¹':
						self.sci_buttons['asin('].setFixedSize(60, 60)
						grid_layout.addWidget(self.sci_buttons['asin('], pos[0], pos[1], pos[2], pos[3])

					elif btnText == 'cos⁻¹':
						self.sci_buttons['acos('].setFixedSize(60, 60)
						grid_layout.addWidget(self.sci_buttons['acos('], pos[0], pos[1], pos[2], pos[3])

					elif btnText == 'tan⁻¹':
						self.sci_buttons['atan('].setFixedSize(60, 60)
						grid_layout.addWidget(self.sci_buttons['atan('], pos[0], pos[1], pos[2], pos[3])

					elif btnText == 'ʸ√x':
						self.sci_buttons['root('].setFixedSize(60, 60)
						grid_layout.addWidget(self.sci_buttons['root('], pos[0], pos[1], pos[2], pos[3])

					elif btnText == 'logₙx':
						self.sci_buttons['logx('].setFixedSize(60, 60)
						grid_layout.addWidget(self.sci_buttons['logx('], pos[0], pos[1], pos[2], pos[3])
					
					elif btnText == 'log₁₀':
						self.sci_buttons['log10('].setFixedSize(60, 60)
						grid_layout.addWidget(self.sci_buttons['log10('], pos[0], pos[1], pos[2], pos[3])

					elif btnText == '!':
						self.sci_buttons['fact('].setFixedSize(60, 60)
						grid_layout.addWidget(self.sci_buttons['fact('], pos[0], pos[1], pos[2], pos[3])
							
					elif btnText == 'eˣ':
						self.sci_buttons['e^'].setFixedSize(60, 60)
						grid_layout.addWidget(self.sci_buttons['e^'], pos[0], pos[1], pos[2], pos[3])
							
					elif btnText == 'x10ˣ':
						self.sci_buttons['*10^'].setFixedSize(60, 60)
						grid_layout.addWidget(self.sci_buttons['*10^'], pos[0], pos[1], pos[2], pos[3])
					
					elif btnText == 'nCr':
						self.sci_buttons['C('].setFixedSize(60, 60)
						grid_layout.addWidget(self.sci_buttons['C('], pos[0], pos[1], pos[2], pos[3])

					elif btnText == 'nPr':
						self.sci_buttons['P('].setFixedSize(60, 60)
						grid_layout.addWidget(self.sci_buttons['P('], pos[0], pos[1], pos[2], pos[3])
					else:
						self.sci_buttons[btnText].setFixedSize(60, 60)
						grid_layout.addWidget(self.sci_buttons[btnText], pos[0], pos[1], pos[2], pos[3])

		return page

	def set_equateLineText(self, text):

		self.equateLine.setText(text)
		self.equateLine.setFocus()

	def equateLineText(self):

		return self.equateLine.text()

	def delete_equateLineText(self):

		x = self.equateLine.text()
		y = x[:-1]
		self.set_equateLineText(y)

	def clear_equateLineText(self):
		
		self.equateLine.setText('')

	def set_ObjectName(self):

		for btnText, btn in self.basic_buttons.items():
			if btnText in ['(', ')', '^2', '/', '*', '.', 'sqrt(']:
				if btnText == '(':
					btn.setObjectName('LPAR')
				elif btnText == ')':
					btn.setObjectName('RPAR')
				elif btnText == '^2':
					btn.setObjectName('SQR')
				elif btnText == '/':
					btn.setObjectName('DIVIDE')
				elif btnText == '*':
					btn.setObjectName('MULTIPLY')
				elif btnText == '.':
					btn.setObjectName('DOT')
				elif btnText == 'sqrt(':
					btn.setObjectName('SQRT')
				
			else:
				if btnText == '=':
					btn.setObjectName('EQUAL')
				elif btnText == '+':
					btn.setObjectName('PLUS')
				else:
					btn.setObjectName(btnText)

		for btnText, btn in self.sci_buttons.items():

			if btnText in ['(', ')', '^2', '/', '*', '.', 'sqrt(']:
				if btnText == '(':
					btn.setObjectName('LPAR')
				elif btnText == ')':
					btn.setObjectName('RPAR')
				elif btnText == '^2':
					btn.setObjectName('SQR')
				elif btnText == '/':
					btn.setObjectName('DIVIDE')
				elif btnText == '*':
					btn.setObjectName('MULTIPLY')
				elif btnText == '.':
					btn.setObjectName('DOT')
				elif btnText == 'sqrt(':
					btn.setObjectName('SQRT')

			elif btnText in ['rnd(', 'tnc(', 'abs(', 'sin(', 'sinh(', 'asin(', 'cos(', 'cosh(', 'acos(', 'tan(', 'tanh(', 'atan(', 'mod(', 'fact(']:
				btn.setObjectName(btnText[:-1])

			elif btnText in ['P(', 'C(', 'root(', 'logx(', 'log10(', 'ln(']:
				btn.setObjectName(btnText[:-1])

			elif btnText in [',', 'e^', '*10^', '^']:
				if btnText == ',':
					btn.setObjectName('COMMA')
				elif btnText == '^':
					btn.setObjectName('RAISE')
				elif btnText == 'e^':
					btn.setObjectName('E')
				elif btnText == '*10^':
					btn.setObjectName('X10')
			
			else:
				if btnText == '=':
					btn.setObjectName('EQUAL')
				elif btnText == '+':
					btn.setObjectName('PLUS')
				else:
					btn.setObjectName(btnText)
	
class About(object):

	def setupUi(self, Form):

		Form.setWindowTitle('About')
		Form.setWindowIcon(QIcon('./resources/window_icon.png'))
		Form.setFixedSize(295, 160)
		#Form.setWindowFlags(Qt.WindowStaysOnTopHint)

		self.label = QLabel(Form)
		self.label.setGeometry(QRect(75, 30, 121, 31))

		font = QFont()
		font.setFamily('Abel')
		font.setPointSize(16)
		font.setBold(True)

		self.label.setFont(font)
		self.label.setText('TEAM BURGIR')

		self.label_2 = QLabel(Form)
		self.label_2.setGeometry(QRect(75, 60, 211, 16))

		font = QFont()
		font.setFamily('Abel')
		font.setPointSize(11)
		font.setBold(True)
		font.setItalic(True)

		self.label_2.setFont(font)
		self.label_2.setText('CALCULATOR PROJECT FOR CCC')

		self.label_3 = QLabel(Form)
		self.label_3.setGeometry(QRect(0, 15, 76, 76))

		self.label_3.setFont(font)
		self.label_3.setText("")
		self.label_3.setPixmap(QPixmap('./resources/window_icon.png'))
		self.label_3.setScaledContents(True)
		self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

		self.label_4 = QLabel(Form)
		self.label_4.setGeometry(QRect(15, 90, 136, 31))

		font = QFont()
		font.setFamily('Century Gothic')
		font.setPointSize(11)

		self.label_4.setFont(font)
		self.label_4.setText('<a href=\"https://github.com/JARalph23Z/Calculator\">GitHub Repository</a>')
		self.label_4.setOpenExternalLinks(True)

		self.label_5 = QLabel(Form)
		self.label_5.setGeometry(QRect(180, 90, 91, 31))

		font = QFont()
		font.setFamily('Century Gothic')
		font.setPointSize(11)

		self.label_5.setFont(font)
		self.label_5.setText("<a href=\"https://drive.google.com/file/d/1ZNi9owFVY8JSgSVuVaDnUNbKqGaqAfF9/view?usp=sharing\">Presentation</a>")
		self.label_5.setOpenExternalLinks(True)

		self.label_6 = QLabel(Form)
		self.label_6.setGeometry(QRect(15, 135, 271, 16))

		font = QFont()
		font.setFamily('Abel')
		font.setPointSize(11)

		self.label_6.setFont(font)
		self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.label_6.setText("| Burgir Calculator ™ |")

class Instructions(object):

	def setupUi(self, Form):

		Form.setWindowTitle('Instructions')
		Form.setFixedSize(480, 717)
		Form.setWindowIcon(QIcon('./resources/window_icon.png'))

		self.widget = QWidget(Form)
		self.widget.setGeometry(QRect(0, 0, 481, 91))
		self.widget.setObjectName("firstWidget")

		self.label = QLabel(self.widget)
		self.label.setGeometry(QRect(45, 0, 91, 91))
		self.label.setText("")
		self.label.setPixmap(QPixmap("./resources/window_icon.png"))
		self.label.setScaledContents(True)

		self.label_2 = QLabel(self.widget)
		self.label_2.setGeometry(QRect(150, 0, 286, 106))

		font = QFont()
		font.setFamily("Abel")
		font.setPointSize(33)
		font.setBold(True)
		font.setItalic(True)
		font.setUnderline(True)

		self.label_2.setFont(font)
		self.label_2.setText("INSTRUCTIONS")

		self.widget_2 = QWidget(Form)
		self.widget_2.setGeometry(QRect(0, 105, 481, 151))
		self.widget_2.setObjectName("secondWidget")

		self.label_3 = QLabel(self.widget_2)
		self.label_3.setGeometry(QRect(45, 15, 166, 16))

		font = QFont()
		font.setFamily("Century Gothic")
		font.setPointSize(12)
		font.setBold(True)

		self.label_3.setFont(font)
		self.label_3.setText("General Instructions")

		self.line = QFrame(self.widget_2)
		self.line.setGeometry(QRect(45, 30, 391, 16))
		self.line.setFrameShape(QFrame.Shape.HLine)
		self.line.setFrameShadow(QFrame.Shadow.Sunken)
		self.line.setObjectName("firstLine")

		self.label_5 = QLabel(self.widget_2)
		self.label_5.setGeometry(QRect(45, 45, 391, 16))

		font = QFont()
		font.setFamily("Century")
		font.setPointSize(10)

		self.label_5.setFont(font)
		self.label_5.setText("•      Be sure to close any parentheses.")

		self.label_6 = QLabel(self.widget_2)
		self.label_6.setGeometry(QRect(45, 60, 391, 31))

		font = QFont()
		font.setFamily("Century")
		font.setPointSize(10)

		self.label_6.setFont(font)
		self.label_6.setWordWrap(True)
		self.label_6.setText("•      Make sure to properly use an operation when using parentheses. 5(5) =/= 5*(5)")

		self.label_7 = QLabel(self.widget_2)
		self.label_7.setGeometry(QRect(45, 90, 391, 16))

		font = QFont()
		font.setFamily("Century")
		font.setPointSize(10)

		self.label_7.setFont(font)
		self.label_7.setText("•     The trigonometric functions are in radians, not degrees.")

		self.label_8 = QLabel(self.widget_2)
		self.label_8.setGeometry(QRect(45, 105, 391, 31))

		font = QFont()
		font.setFamily("Century")
		font.setPointSize(10)

		self.label_8.setFont(font)
		self.label_8.setWordWrap(True)
		self.label_8.setText("•     You can opt to change or disable the button click sound in Preferences > Button Sound.")

		self.line_2 = QFrame(self.widget_2)
		self.line_2.setGeometry(QRect(60, 150, 391, 16))
		self.line_2.setFrameShape(QFrame.Shape.HLine)
		self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
		self.line_2.setObjectName('secondLine')

		self.widget_3 = QWidget(Form)
		self.widget_3.setGeometry(QRect(0, 270, 481, 241))
		self.widget_3.setObjectName("thirdWidget")

		self.label_4 = QLabel(self.widget_3)
		self.label_4.setGeometry(QRect(45, 15, 181, 16))

		font = QFont()
		font.setFamily("Century Gothic")
		font.setPointSize(12)
		font.setBold(True)

		self.label_4.setFont(font)
		self.label_4.setText("Calculator Instructions")

		self.line_3 = QFrame(self.widget_3)
		self.line_3.setGeometry(QRect(45, 30, 391, 16))
		self.line_3.setFrameShape(QFrame.Shape.HLine)
		self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
		self.line_3.setObjectName("thirdLine")

		self.pushButton = QPushButton(self.widget_3)
		self.pushButton.setGeometry(QRect(45, 45, 46, 46))
		self.pushButton.setText("ANS")
		self.pushButton.setObjectName("instButton1")

		self.label_9 = QLabel(self.widget_3)
		self.label_9.setGeometry(QRect(105, 45, 121, 46))

		font = QFont()
		font.setFamily("Century")

		self.label_9.setFont(font)
		self.label_9.setWordWrap(True)
		self.label_9.setText("Adds the last calculated result to the display.")

		self.line_4 = QFrame(self.widget_3)
		self.line_4.setGeometry(QRect(225, 45, 30, 181))
		self.line_4.setFrameShape(QFrame.Shape.VLine)
		self.line_4.setFrameShadow(QFrame.Shadow.Sunken)
		self.line_4.setObjectName("fourthLine")

		self.label_10 = QLabel(self.widget_3)
		self.label_10.setGeometry(QRect(105, 105, 121, 46))

		font = QFont()
		font.setFamily("Century")

		self.label_10.setFont(font)
		self.label_10.setWordWrap(True)
		self.label_10.setText("Deletes the last item in the display.")

		self.pushButton_2 = QPushButton(self.widget_3)
		self.pushButton_2.setGeometry(QRect(45, 105, 46, 46))
		self.pushButton_2.setText("DEL")
		self.pushButton_2.setObjectName("instButton2")
		
		self.label_11 = QLabel(self.widget_3)
		self.label_11.setGeometry(QRect(105, 165, 121, 46))

		font = QFont()
		font.setFamily("Century")

		self.label_11.setFont(font)
		self.label_11.setWordWrap(True)
		self.label_11.setText("Deletes everything in the display.")
		
		self.pushButton_3 = QPushButton(self.widget_3)
		self.pushButton_3.setGeometry(QRect(45, 165, 46, 46))
		self.pushButton_3.setText("AC")
		self.pushButton_3.setObjectName("instButton3")
		
		self.label_12 = QLabel(self.widget_3)
		self.label_12.setGeometry(QRect(315, 45, 121, 46))

		font = QFont()
		font.setFamily("Century")

		self.label_12.setFont(font)
		self.label_12.setWordWrap(True)
		self.label_12.setText("Parentheses buttons. Required when using functions.")
			

		self.pushButton_4 = QPushButton(self.widget_3)
		self.pushButton_4.setGeometry(QRect(255, 45, 46, 46))
		self.pushButton_4.setText("( )")
		self.pushButton_4.setObjectName("instButton4")

		self.pushButton_5 = QPushButton(self.widget_3)
		self.pushButton_5.setGeometry(QRect(255, 105, 46, 46))
		self.pushButton_5.setText("=")
		self.pushButton_5.setObjectName("instButton5")
		
		self.label_13 = QLabel(self.widget_3)
		self.label_13.setGeometry(QRect(315, 105, 121, 46))

		font = QFont()
		font.setFamily("Century")

		self.label_13.setFont(font)
		self.label_13.setWordWrap(True)
		self.label_13.setText("Calculates the equations in the display and stores it.")
		
		self.label_14 = QLabel(self.widget_3)
		self.label_14.setGeometry(QRect(315, 165, 121, 46))

		font = QFont()
		font.setFamily("Century")

		self.label_14.setFont(font)
		self.label_14.setWordWrap(True)
		self.label_14.setText("Necessary for functions that require two numbers.")

		self.pushButton_6 = QPushButton(self.widget_3)
		self.pushButton_6.setGeometry(QRect(255, 165, 46, 46))
		self.pushButton_6.setText(",")
		self.pushButton_6.setObjectName("instButton6")
		
		self.widget_4 = QWidget(Form)
		self.widget_4.setGeometry(QRect(0, 525, 481, 46))
		self.widget_4.setObjectName("fourthWidget")
		
		self.label_15 = QLabel(self.widget_4)
		self.label_15.setGeometry(QRect(45, 0, 391, 46))

		font = QFont()
		font.setFamily("Century")

		self.label_15.setFont(font)
		self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.label_15.setWordWrap(True)
		self.label_15.setText("Some buttons will also show a status message when hovered with their instructions for convenience. Read and follow accordingly.")
		
		self.widget_5 = QWidget(Form)
		self.widget_5.setGeometry(QRect(0, 585, 481, 61))
		self.widget_5.setObjectName("fifthWidget")
		
		self.label_16 = QLabel(self.widget_5)
		self.label_16.setGeometry(QRect(45, 0, 391, 61))

		font = QFont()
		font.setFamily("Century")

		self.label_16.setFont(font)
		self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.label_16.setWordWrap(True)
		self.label_16.setText("<html><head/><body><p><span style=\" font-weight:700;\">Pro Tip!</span> You can also type directly to the display. Just make sure to follow the general instructions and <span style=\" font-style:italic;\">don\'t use spaces.</span> You can also press Enter to calculate the display automatically.</p></body></html>")
		
		self.widget_6 = QWidget(Form)
		self.widget_6.setGeometry(QRect(0, 660, 481, 46))
		self.widget_6.setObjectName("sixthWidget")
		
		self.label_17 = QLabel(self.widget_6)
		self.label_17.setGeometry(QRect(30, 0, 421, 46))

		font = QFont()
		font.setFamily("Abel")
		font.setPointSize(14)
		font.setBold(True)

		self.label_17.setFont(font)
		self.label_17.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.label_17.setWordWrap(True)
		self.label_17.setText("We hope you like our calculator! - Team Burgir")

class Menu:

	def __init__(self, MainWindow):

		super().__init__()

		self.view = MainWindow
		self.menuBar()
		self.actionSignals()

	def menuBar(self):

		self.menuBar = QMenuBar()
		self.menuBar.setGeometry(QRect(0, 0, 277, 22))
		self.view.setMenuBar(self.menuBar)

		## Set Up the Buttons in Main Menu Bar
		self.m_SelectCalculator = QMenu(self.menuBar)
		self.m_SelectCalculator.setTitle('Select Calculator')

		# Preferences
		self.m_Preferences = QMenu(self.menuBar)
		self.m_Preferences.setTitle('Preferences')

		# Help
		self._Help = QMenu(self.menuBar)
		self._Help.setTitle('Help')

		# Sub Menu = Button Sound
		self.m_m_ButtonSound = QMenu(self.m_Preferences)
		self.m_m_ButtonSound.setTitle('Button Sound')

		# Set up QActionGroup for Sub Menu Button Sound
		self.soundGroup = QActionGroup(self.m_m_ButtonSound)
		self.soundGroup.setObjectName('soundGroup')

		## Set Up the Buttons in Select Calculator
		
		# Scientific Calculator
		self.a_ScientificCalculator = QAction(self.menuBar)
		self.a_ScientificCalculator.setText('Scientific Calculator')
		self.a_ScientificCalculator.setStatusTip('Please wait patiently.')
		self.a_ScientificCalculator.setCheckable(True)
		self.a_ScientificCalculator.setChecked(False)
		self.a_ScientificCalculator.setShortcut('Ctrl+1')

		## Set Up the Buttons in Help

		# Instructions
		self.a_Instructions = QAction(self.menuBar)
		self.a_Instructions.setText('Instructions')
		self.a_Instructions.setShortcut('Ctrl+3')

		# About
		self.a_About = QAction(self.menuBar)
		self.a_About.setText('About')
		self.a_About.setShortcut('Ctrl+4')
		
		## Sub Buttons in Sub Menu "Button Sound"

		sounds = ['Normal', 'Burgir', 'Disable']
		for sound in sounds:
			action = QAction(sound, self.m_m_ButtonSound, checkable = True, checked = sound == sounds[0])
			action.setData(sound + '.mp3')
			self.m_m_ButtonSound.addAction(action)
			self.soundGroup.addAction(action)

		## Dark Theme
		self.a_Dark = QAction(self.menuBar)
		self.a_Dark.setText('Dark Theme')
		self.a_Dark.setCheckable(True)
		self.a_Dark.setChecked(False)
		self.a_Dark.setShortcut('Ctrl+2')

		## Set Up the Order of Buttons

		# Main Buttons
		self.menuBar.addAction(self.m_SelectCalculator.menuAction())
		self.menuBar.addAction(self.m_Preferences.menuAction())
		self.menuBar.addAction(self._Help.menuAction())

		# Sub Buttons = Select Calculator
		self.m_SelectCalculator.addAction(self.a_ScientificCalculator)

		# Sub Buttons = Preferences
		self.m_Preferences.addAction(self.a_Dark)
		self.m_Preferences.addAction(self.m_m_ButtonSound.menuAction())


		# Sub Buttons = Help
		self._Help.addAction(self.a_Instructions)
		self._Help.addAction(self.a_About)

	def actionSignals(self):

		self.a_About.triggered.connect(self.action_About)
		self.a_Instructions.triggered.connect(self.action_Instructions)
		self.a_ScientificCalculator.triggered.connect(self.action_ScientificCalculator)
		self.a_Dark.triggered.connect(self.action_Dark)

	def action_Dark(self, checked):

		if checked:
			
			with open('./resources/theme_2.qss', 'r') as f:

				style = f.read()
				app.setStyleSheet(style)

		else:

			with open('./resources/theme.qss', 'r') as f:

				style = f.read()
				app.setStyleSheet(style) 

	def action_About(self):

		self.x = QMainWindow(self.view)
		self.y = About()
		self.y.setupUi(self.x)
		self.x.show()

	def action_Instructions(self):

		self.x = QMainWindow(self.view)
		self.y = Instructions()
		self.y.setupUi(self.x)
		self.x.show()

	def action_ScientificCalculator(self, checked):

		if checked:
			self.view.stacked_widget.setCurrentIndex(1)
			self.view.setFixedSize(710, 485)
			self.view.setMaximumSize(710, 485)
		else:
			self.view.stacked_widget.setCurrentIndex(0)
			self.view.setFixedSize(380, 485)
			self.view.setMaximumSize(380, 485)

class StatusBar:

	def __init__(self, MainWindow):

		super().__init__()

		self.view = MainWindow
		self.statusBar = QStatusBar()
		self.statusBar.setSizeGripEnabled(False)
		self.statusBar.setFixedHeight(35)
		self.view.setStatusBar(self.statusBar)
		self.statusBar.showMessage('Help > Instructions', 0)
		self.statusTips()
		self.date_and_time()

	def statusTips(self):

		self.view.sci_buttons['rnd('].setStatusTip('Round x to yᵗʰ place. Leave y blank to round to nearest integer: rnd(x, y)')
		self.view.sci_buttons['tnc('].setStatusTip('Transform x to integer, regardless of decimals: tnc(29.5) = 29')
		self.view.sci_buttons['abs('].setStatusTip('Gives the absolute of x: abs(x)')
		self.view.sci_buttons['C('].setStatusTip('Gives the total number of combinations of two numbers: C(x, y)')
		self.view.sci_buttons['P('].setStatusTip('Gives the total number of permutations of two numbers: P(x, y)')
		self.view.sci_buttons['^'].setStatusTip('Raise x to the nᵗʰ power: 5^2 = 25')
		self.view.sci_buttons['root('].setStatusTip('Gives the yᵗʰ root of x: root(x, y) = root(125, 3) = 5')
		self.view.sci_buttons['fact('].setStatusTip('Gives the factorial of a number: fact(x)')
		self.view.sci_buttons['e^'].setStatusTip('Raise e to the nᵗʰ power: e^x')
		self.view.sci_buttons['mod('].setStatusTip('Gives the remainder when x is divided by y: mod(5, 2) = 1')
		self.view.sci_buttons['logx('].setStatusTip('Gives the logarithm of x with base n: logx(x, n)')
		self.view.sci_buttons['log10('].setStatusTip('Gives the logarithm of x with base 10: log10(x)')
		self.view.sci_buttons['ln('].setStatusTip('Gives the logarithm of x with base e: ln(x)')
		self.view.sci_buttons['asin('].setStatusTip('Number must only be between 1 and -1: asin(0.5)')
		self.view.sci_buttons['acos('].setStatusTip('Number must only be between 1 and -1: acos(0.5)')
		self.view.sci_buttons['atan('].setStatusTip('Number must only be between 1 and -1: atan(0.5)')

		self.view.sci_buttons['sin('].setStatusTip('Trigonometric functions are in radians, not degrees.')
		self.view.sci_buttons['cos('].setStatusTip('Trigonometric functions are in radians, not degrees.')
		self.view.sci_buttons['tan('].setStatusTip('Trigonometric functions are in radians, not degrees.')
		self.view.sci_buttons['sinh('].setStatusTip('Trigonometric functions are in radians, not degrees.')
		self.view.sci_buttons['cosh('].setStatusTip('Trigonometric functions are in radians, not degrees.')
		self.view.sci_buttons['tanh('].setStatusTip('Trigonometric functions are in radians, not degrees.')

	def date_and_time(self):

		x = QDateTime.currentDateTime()
		self.current = QLabel()
		self.current.setObjectName('DateTime')
		self.current.setText(x.toString())
		self.font = QFont()
		self.font.setFamily('Century Gothic')
		self.font.setPointSize(9)
		self.current.setFont(self.font)
		self.statusBar.addPermanentWidget(self.current, stretch = 0)

		self.update()
		self.timer = QTimer()
		self.timer.timeout.connect(self.update)
		self.timer.start(1000)

		self.instructions()
		self.timer2 = QTimer()
		self.timer2.timeout.connect(self.instructions)
		self.timer2.start(10000)

	def update(self):

		_current = QDateTime.currentDateTime()
		self.current.setText(_current.toString())

	def instructions(self):

		self.statusBar.showMessage('Help > Instructions', 0)

class Controller:

	def __init__(self, MainWindow):

		self.view = MainWindow
		self.stored = ''

		self.connectSignals()
		self.connectSignals_adv()
		self.connectSignals_extra()

	def playsound(self):
		checkbox = self.view.findChild(QActionGroup, 'soundGroup')
		if checkbox.checkedAction().text() == 'Disable':
			return
		else:
				playsound('./resources/' + checkbox.checkedAction().data(), False)

	def handleStore(self):

		if self.result != 'ERROR':
			self.stored = self.view.equateLineText()

	def handleReturn(self):

		self.buildExpression(self.stored)

	def buildExpression(self, sub_exp):

		if self.view.equateLineText() == 'ERROR':
			self.view.clear_equateLineText()

		text = self.view.equateLineText()
		text = list(str(text))
		pos = self.view.equateLine.cursorPosition()
		text.insert(pos, sub_exp)
		expression = ''.join(text)

		self.view.set_equateLineText(expression)

	def calculateResult(self):

		self.result = str(calculator.Calculate(str(self.view.equateLineText())))
		if self.result[-2:] == '.0':
			self.view.set_equateLineText(self.result[:-2])
		else:
			self.view.set_equateLineText(self.result)

	def connectSignals(self):

		for btnText, btn in self.view.basic_buttons.items():

			if btnText == '=':
				self.view.basic_buttons['='].clicked.connect(self.calculateResult)
				self.view.basic_buttons['='].clicked.connect(self.handleStore)
				self.view.basic_buttons['='].clicked.connect(self.playsound)

			elif btnText == 'AC':
				self.view.basic_buttons['AC'].clicked.connect(self.view.clear_equateLineText)
				self.view.basic_buttons['AC'].clicked.connect(self.playsound)					

			elif btnText == 'DEL':
				self.view.basic_buttons['DEL'].clicked.connect(self.view.delete_equateLineText)
				self.view.basic_buttons['DEL'].clicked.connect(self.playsound)	

			elif btnText == 'ANS':
				self.view.basic_buttons['ANS'].clicked.connect(self.handleReturn)
				self.view.basic_buttons['ANS'].clicked.connect(self.playsound)

			else:
				btn.clicked.connect(partial(self.buildExpression, btnText))
				btn.clicked.connect(self.playsound)				

	def connectSignals_adv(self):

		for btnText, btn in self.view.sci_buttons.items():

			if btnText == '=':
				self.view.sci_buttons['='].clicked.connect(self.calculateResult)
				self.view.sci_buttons['='].clicked.connect(self.handleStore)
				self.view.sci_buttons['='].clicked.connect(self.playsound)

			elif btnText == 'AC':
				self.view.sci_buttons['AC'].clicked.connect(self.view.clear_equateLineText)
				self.view.sci_buttons['AC'].clicked.connect(self.playsound)

			elif btnText == 'DEL':
				self.view.sci_buttons['DEL'].clicked.connect(self.view.delete_equateLineText)
				self.view.sci_buttons['DEL'].clicked.connect(self.playsound)

			elif btnText == 'ANS':
				self.view.sci_buttons['ANS'].clicked.connect(self.handleReturn)
				self.view.sci_buttons['ANS'].clicked.connect(self.playsound)

			else:
				btn.clicked.connect(partial(self.buildExpression, btnText))
				btn.clicked.connect(self.playsound)

	def connectSignals_extra(self):

		self.view.equateLine.returnPressed.connect(self.calculateResult)



app = QApplication(sys.argv)

def background():
	while True:
		playsound('./resources/background.mp3')

def main():

	run = CalculatorUI()
	Controller(run)
	m = Menu(run)
	s = StatusBar(run)

	Thread(target = background, daemon = True).start()

	run.show()

	with open('./resources/theme.qss', 'r') as f:

		style = f.read()
		app.setStyleSheet(style)
	sys.exit(app.exec())