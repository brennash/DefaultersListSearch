import io
import os
import sys
import csv
import datetime
import re
import json
import smtplib
import logging
import pickle
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
	print 'SEARCH REQUEST'
	print len(jsonList),' records'

	if request.method == 'POST':
		print 'POST REQUEST'
		print request.form.get("search_string")
		print request.data,"REQUEST DATA"
	
		return 'Result'
	else:
		print 'GET REQUEST'
		return redirect(url_for('index'))

def parseDirectory(verbose, directory):
	global jsonList
	filePaths = []
	jsonList  = []
	for root, directories, files in os.walk(directory):
		for filename in files:
			if '.xls' in filename:
				filepath = os.path.join(root, filename)
				filePaths.append(os.path.dirname(os.path.abspath(filepath))+os.path.sep+filename)

	readExcel = ReadExcel()
	for fileName in filePaths:
		jsonOutput = readExcel.parseFile(fileName)
		jsonList   = jsonList + jsonOutput

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
