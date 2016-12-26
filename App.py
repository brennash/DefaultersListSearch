import io
import os
import csv
import datetime
import re
import json
import smtplib
import logging
import pickle
import requests
from flask import render_template
from flask import session
from flask import make_response, send_from_directory, redirect, url_for
from flask import Flask, request, Response
from functools import wraps
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Setup the app, with a random secret key for the sessions
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024
app.secret_key = os.urandom(24).encode('hex')

# Setup the search engine
searchEngine = None

# The main index page
@app.route('/')
def index():
	dateString = datetime.datetime.now().strftime('%Y%m%d %H:%M:%S')
	session['index-page'] = (dateString)
	return render_template('index.html')

@app.route('/search/', methods=['GET','POST'])
def search():
	if request.method == 'POST':
		# Grab the request parameters
		requestString = str(request.form.get('search_string'))
		print requestString, 'request string'

		#r = requests.post("http://localhost:1798/api/search/", data={'number': 12524, 'type': 'issue', 'action': 'show'})
		#print(r.status_code, r.reason)

		res = requests.post('http://localhost:1798/api/search/', data={'search_string':requestString})
		print 'response from server:',res.text
		#dictFromServer = res.json()
		#print 'Request String:',requestString
		#return redirect(url_for('index'))
		return 'Success!'
	else:
		return redirect(url_for('index'))

def getJSON(inputString):
	outputDict = {}
	outputDict['search_terms'] = inputString
	return outputDict

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=1916, debug=True)
