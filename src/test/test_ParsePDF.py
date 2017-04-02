import sys
import logging
import unittest
import datetime
from ParsePDF import ParsePDF

class Test(unittest.TestCase):

	def test_initSetup(self):
		""" 
		Tests the test class itself to verify it is working. 
		Should all other tests fail, at least this test should pass.
		"""
		self.assertTrue(True)
	
	def test_Parser_1(self):
		""" 
		This test function looks to load in an example configuration
		file and test the getter functions to return config information. 
		"""
		parser = ParsePDF()
		self.assertIsNotNone(parser)

	def test_isNewLine_1(self):
		""" 
		This test function looks to load in an example configuration
		file and test the getter functions to return config information. 
		"""
		parser = ParsePDF()
		line   = '  Name  Address   Fine'
		result = parser.isNewLine(line)
		self.assertFalse(result)

	def test_isNewLine_2(self):
		""" 
		This test function looks to load in an example configuration
		file and test the getter functions to return config information. 
		"""
		parser = ParsePDF()
		line   = 'MICK NUGENT     1 MAIN STREET, DUBLIN    400.00'
		result = parser.isNewLine(line)
		self.assertTrue(result)


	def test_isNewLine_3(self):
		""" 
		This test function looks to load in an example configuration
		file and test the getter functions to return config information. 
		"""
		parser = ParsePDF()
		line   = '    MICK NUGENT     1 MAIN STREET, DUBLIN    400.00'
		result = parser.isNewLine(line)
		self.assertTrue(result)

	def test_isNewLine_4(self):
		parser = ParsePDF()
		line = '                         CASTLEKNOCK, DUBLIN 15'
		result = parser.isNewLine(line)
		self.assertFalse(result)

	def test_isNewLine_5(self):
		parser = ParsePDF()
		line = '                       FOXROCK, DUBLIN 18                              RENTING/DIRECTOR '
		result = parser.isNewLine(line)
		self.assertFalse(result)

	def test_MultiLine_Parser_1(self):
		parser     = ParsePDF()
		inputFile  = 'data/txts/defaulters-list1-september2015.txt'
		inputLines = parser.parseText(inputFile)
		testStr    = None
		for inputLine in inputLines:
			if 'THE CASTLE INN' in inputLine:
				testStr = inputLine
				break

		self.assertIsNotNone(testStr)

	def test_MultiLine_Parser_2(self):
		parser     = ParsePDF()
		inputFile  = 'data/txts/defaulters-list1-september2015.txt'
		inputLines = parser.parseText(inputFile)
		testStr    = ''
		for inputLine in inputLines:
			if 'THE CASTLE INN' in inputLine:
				testStr = inputLine

		self.assertTrue('TIPPERARY' in testStr)
