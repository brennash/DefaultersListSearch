import re
import os
import csv
import sys
import json
import logging
import datetime
from sets import Set
from optparse import OptionParser
from logging.handlers import RotatingFileHandler

class ParsePDF:

	def __init__(self):
		self.verbose       = False
		self.logger        = None

		self.chargeList = ['ILLEGAL SELLING OF CIGARETTES',
			'POSSESSION OF ',
			'FAILURE TO ',
			'CLAIMING VAT ',
			'DELIVERING INCORRECT ',
			'PRODUCING INCORRECT ',
			'OBSTRUCTION OF REVENUE OFFICER',
			'ALCOHOL SMUGGLING',
			'ILLEGAL BETTING ',
			'FAILURE TO COMPLY',
			'CIGARETTE SMUGGLING',
			'SELLING UNTAXED ALCOHOL',
			'POSSESSION OF COUNTERFEIT ALCOHOL FOR SALE',
			'CLAIMING INCOME TAX REPAYMENT(S) ',
			'TO WHICH NOT ENTITLED',
			'SELLING UNTAXED ALCOHOL',
			'MISUSE OF ',
			'PRODUCTION OF ']

	def start(self, inputFilename, verboseFlag=False):
		self.verbose  = verboseFlag
		self.setupLogging()
		defaulterList = self.parseText(inputFilename)

		for defaulter in defaulterList:
			print defaulter


		#self.logger.info('Finished processing {0} defaulters in {1}'.format(len(defaulterList), inputFilename))
		#return defaulterList

	def setupLogging(self):
		self.logger = logging.getLogger(__name__)
		handler = RotatingFileHandler('log/parse_pdf.log', maxBytes=500000, backupCount=3)
		format  = "%(asctime)s %(levelname)-8s %(message)s"
		handler.setFormatter(logging.Formatter(format))
		handler.setLevel(logging.INFO)
		self.logger.addHandler(handler)
		self.logger.setLevel(logging.INFO)

	def setLogLevel(self, logLevel):
		self.logger.setLevel(logLevel)

	def parseText(self, inputFilename):
		""" Parses the input file, converted using the command 
		    pdftotext -layout <filename> 
		"""

		# Open the input text file for parsing
		if not os.path.isfile(inputFilename):
			self.logger.error('Cannot open file {0}'.format(inputFilename))
		else:
			inputFile  = open(inputFilename, 'rb')
			if self.logger is not None:
				self.logger.info('Processing {0} input file'.format(inputFilename))
			index        = 0
			inputLines   = []
			prevLines    = ''

			for line in inputFile:
				if self.isNewLine(line) and not self.isCharge(line):
					if len(line.lstrip().rstrip()) < 20:
						lastLine = inputLines[-1]
						lastLine = lastLine + line
						inputLines[-1] += lastLine
					else:
						inputLines.append(prevLines+line)
						prevLines = ''
				else:
					prevLines += line
				index += 1

			lastLine = inputLines[-1]
			lastLine = lastLine + line
			inputLines[-1] += lastLine

		return inputLines

	def isCharge(self, line):
		for charge in self.chargeList:
			if charge in line:
				return True
		return False

	def isNewLine(self, line):
		regex = re.compile('^\s{0,6}[A-Z0-9\',.]{1,20}\s+')

		# Remove any charges from the list
		for charge in self.chargeList:
			if charge in line:
				return False

		# Remove the header
		if 'Address' in line or 'Name' in line:
			return False

		# Check the regex
		if regex.match(line):
			return True
		else:
			return False




	def replaceChars(self, line):
		result = ''
		regex = re.compile('[A-Z0-9,]')
		for char in line:
			if regex.match(char):
				result += 'X'
			else:
				result += char
		return result

	def getIndexOfRegex(self, line, regexStr, includeRegexLen=False):
		tokens = line.split()
		regex  = re.compile(regexStr)
		for token in tokens:
			if regex.match(token):
				regexIndex = line.index(token)
				if includeRegexLen:
					regexIndex += len(token)
				return regexIndex
		return -1

	def isValidLine(self, line):
		regex1         = re.compile('^\s*[A-Z]+')
		if regex1.match(line) and 'FAILURE' not in line and 'Address' not in line:
			return True
		return False

	def splitLine(self, line):
		prevChar = ''
		tokens   = []
		prevWord = ''
		newWord  = False

		for char in line:
			if char != ' ' and prevChar == ' ' and newWord:
				tokens.append(prevWord.rstrip().lstrip())
				prevWord = char
				newWord  = False
			elif char == ' ' and prevChar == ' ':
				newWord  = True
			elif char != ' ' and prevChar != ' ':
				prevWord += char
				newWord  = False
			else:
				prevWord += char

			prevChar = char

		tokens.append(prevWord)

		return tokens

	def isCompanyNumber(self, line):
		regex     = re.compile('^\d+$')
		cleanLine = line.lstrip().rstrip().replace(' ','').replace('\t','')
		if regex.match(cleanLine):
			return True
		return False

	def isDate(self, line):
		regex  = re.compile('^\d+\s*/\s*\d+\s*/\s*\d+')
		cleanLine = line.lstrip().rstrip()
		if regex.match(cleanLine):
			return True
		return False

	def isEmptyLine(self, line):
		regex  = re.compile('^\s*$')
		cleanLine = line.lstrip().rstrip()
		if regex.match(cleanLine):
			return True
		return False

	def splitCompanyNames(self, list):
		element1   = ''
		element2   = ''
		nameList   = []
		resultList = []

		for element3 in list:
			if element1.upper() == 'LIMITED' and element2.upper() == 'ACTIVITY' and element3.upper() == 'COMPANY':
				nameList.append(element3)
				resultList.append(' '.join(nameList))
			element1 = element2
			element2 = element3

		return []

	def scrapeWebData(self):
		""" Interates though the companies list, scraping the details of each in turn.
		"""

		# The list of json elements
		jsonList = []

		for index, company in enumerate(self.companies):
			companyName = company.getName()
			# self.logger.info('Scraping data on {0} ({1})'.format(companyName, index))
			self.scrapeDetails(index)
			jsonData = self.companies[index].getDetails()
			jsonList.append(jsonData)

		# Log the results returned
		self.logger.info('Returning JSON company data in list of {0} elements'.format(len(jsonList)))

		# Return a list that on each line has a JSON company structure
		return jsonList


def main(argv):
	parser = OptionParser(usage="Usage: ParsePDF [-v|--verbose] <text-file>")

	parser.add_option("-v", "--verbose",
		action="store_true",
		dest="verboseFlag",
		default=False,
		help="verbose output, report errors/issues")

	(options, filename) = parser.parse_args()

	if len(filename) != 1:
       	        print parser.print_help()
               	exit(1)
	elif not os.path.isfile(filename[0]) :
		print parser.print_help()
		print 'Input file does not exist...'
		exit(1)
	elif '.txt' not in filename[0]:
		print parser.print_help()
		print 'Input file needs to be a *.txt file...'
		exit(1)
	else:
		check = ParsePDF()
		check.start(filename[0], options.verboseFlag)

if __name__ == "__main__":
    sys.exit(main(sys.argv))

