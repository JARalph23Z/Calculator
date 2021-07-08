import sys
import math
import operator
from threading import Thread 
from playsound import playsound
from functools import partial
from pyparsing import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

import calculator
import ui

if __name__ == '__main__':
	ui.main()