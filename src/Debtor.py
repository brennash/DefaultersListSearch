import unicodedata
import regex

class Debtor:

	def __init__(self, header, valueList):

		self.header = header
		self.name   = self.removeNonAscii(valueList[0])
		self.addr   = self.removeNonAscii(valueList[1])

	def removeNonAscii(self, inputText):
		if inputText is None:
			return ''
		elif type(inputText) is unicode:
			return unicodedata.normalize('NFKD', inputText).encode('ascii','ignore')
		else:
			return str(inputText)

#		return unicodedata.normalize('NFKD',unicode(inputText,"ISO-8859-1")).encode("ascii","ignore")
#		return regex.sub(r"\p{Mn}", "", unicodedata.normalize("NFKD", inputText))

	def getName(self):
		""" Returns the name value as a string.
		"""
		return self.name


	def printDetails(self):

		print '{0},{1},{2}'.format(self.name, self.addr, self.header)
