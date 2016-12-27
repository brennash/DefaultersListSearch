import io
import os
import sys
import csv
import datetime
import re
import json
import string
import smtplib
import logging
import pickle
from sets import Set
from ReadExcel import ReadExcel
from optparse import OptionParser
from flask import render_template
from flask import session
from flask import make_response, send_from_directory, redirect, url_for
from flask import Flask, request, Response
from functools import wraps
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# The global variables holding the json records
global jsonList
global wordList

# Setup the app, with a random secret key for the sessions
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024
app.secret_key = os.urandom(24).encode('hex')

# The main index page
@app.route('/')
def index():
	return 'This is the search API index...'

@app.route('/api/search/', methods=['POST'])
def search():
	print len(jsonList),' records'

	if request.method == 'POST':
		print 'POST REQUEST'
		searchString = request.form.get("search_string")
		responseList = getSearchList(searchString)
		return responseList
	else:
		print 'GET REQUEST'
		return redirect(url_for('index'))

def getSearchList(searchString):
	global jsonList
	global wordList

	print 'JSONLIST LEN',len(jsonList)
	print 'WORDLIST LEN',len(wordList)

	searchString = searchString.replace(',',' ')
	searchString = searchString.replace(':',' ')
	searchString = searchString.replace('\t',' ')
	searchTokens = searchString.split(' ')
	totalIndexes = Set()
	for token in searchTokens:
		if token.upper() in wordList.keys():
			indexSet = wordList[token]
			if len(totalIndexes) == 0:
				totalIndexes = indexSet
			else:
				totalIndexes = totalIndexes.intersection(indexSet)

	print 'Len of indexes',len(totalIndexes)

	resultList = []
	for element in totalIndexes:
		resultList.append(jsonList[element])

	return json.dumps(resultList)

def parseDirectory(verbose, directory):
	# Setup the global variable holding the JSON
	global jsonList
	jsonList  = []

	# The list of Excel files
	filePaths = []

	# Go through the data directory looking for Excel files
	for root, directories, files in os.walk(directory):
		for filename in files:
			if '.xls' in filename:
				filepath = os.path.join(root, filename)
				filePaths.append(os.path.dirname(os.path.abspath(filepath))+os.path.sep+filename)

	# Now read each file and extract the data
	readExcel = ReadExcel()
	for fileName in filePaths:
		jsonOutput = readExcel.parseFile(fileName)
		jsonList   = jsonList + jsonOutput

	# Lastly, define a hash set for each word in the output
	createHashSet()

def createHashSet():
	global jsonList
	global wordList
	wordList = {}
	addedWords = Set()

	for index, jsonString in enumerate(jsonList):
		jsonElement = json.loads(jsonString)
		name    = jsonElement['name']
		address = jsonElement['address']

		name  = name.replace("\'","'")
		name  = name.translate(string.punctuation)
		address  = address.translate(string.punctuation)

		tokens = name.split(' ') + address.split(' ')
		for token in tokens:
			if token.upper() not in addedWords:
				indexSet = Set()
				indexSet.add(index)
				wordList[token.upper()] = indexSet
				addedWords.add(token.upper())
			else:
				indexSet = wordList[token.upper()] 
				indexSet.add(index)
				wordList[token.upper()] = indexSet

def main(argv):
	# Setup the search engine
	jsonList = []

        parser = OptionParser(usage="Usage: SearchEngine <directory>")

        parser.add_option("-v", "--verbose",
                action="store_true",
                dest="verboseFlag",
                default=False,
                help="Verbose output from the search engine")

        (options, filename) = parser.parse_args()

        if len(filename) != 1 or not os.path.isdir(filename[0]) :
                print parser.print_help()
                exit(1)

	# Build the set of terms and records
	parseDirectory(options.verboseFlag, filename[0])

	# Now run the application
	app.run(host='0.0.0.0', port=1798, debug=options.verboseFlag)
                
if __name__ == "__main__":
    sys.exit(main(sys.argv))
