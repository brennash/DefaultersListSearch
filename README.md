# DefaultersListSearch
This project is a Python Flask micro-service to provide a searchable web-front end to the Excel-based defaulters data. Effectively 
the platform provides a limited search engine to match records based on the name or other details within the data. 

# Installation
The installation of this system requires a number of steps, and has is ideally installed on a Linux/Mac OSX environment. Installing 
and running the necessary packages under a Windows-based environment has not been tested. After cloning the project using git clone, 
open a terminal and go to the project directory. 

```
	cd DefaultersListSearch
	virtualenv venv
	. venv/bin/activate
	pip install Flask openpyxl unidecode regex requests
	./bin/getExcelData.sh
```

This should create a virtual environment in which to run the project, and install the necessary packages into this environment 
using the pip package installer. If you're behind a firewall or have limited network access then you might have problems with 
this install. The call to the getExcelData.sh script runs a series of wget commands to download the defaulters Excel data into 
the data sub-folder for later parsing. 

# Running the platform
There are two Flask components which need to be started to run the platform, 

* SearchEngine.py - which parses through the Excel documents and maintains the searchable dataset.  
* App.py - which provides the search front-end. 

```
	./bin/startSearch.sh
```

## Screenshots
Below is a screenshot of the main query web front-end. 
![Alt text](/static/img/screenshot.png?raw=true "Screenshot")

