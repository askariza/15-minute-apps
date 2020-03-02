import sys
import unittest
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtTest import QTest
from PyQt5.QtCore import *
import minesweeper

app = QApplication(sys.argv)

class PosTest(unittest.TestCase):
	
	def setUp(self):
		self.form = minesweeper.MainWindow()

	def test_reset_function(self):




if __name__ == '__main__':
	unittest.main()
