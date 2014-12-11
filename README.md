2014
----
7th Semester
------
Course : Architecture of Open Source Application
---------
Instructor : Dr. Ram P Rustagi
--------
Team:
Pratheek MS
Chitra Singh
Anushree Prasanna Kumar
--------------------

Project Title : Alex
====================

Description
-----------
 Alex is an open source Natural Language Processing based command line access tool.

Installation
------------
 To install alex just run the following in your terminal:
      git clone https://github.com/pratheekms/alex 
 Navigate to alex directory and run setup.py :
      python setup.py

Modules
-------
Alex contains the following files (modules):
1. README - This readme file.
2. setup.py - contains code to copy files and install alex to your home or a custom directory.
3. LICENSE - Licensing information
4. alex - subdirectory containing files to process queries and perform operations.
   Within alex :-
		1. corpus.txt - contains corpus of queries in different forms for alex 
		2. category.txt - contains list of categories the processed queries can be mapped to (eg. count lines,file info etc)
		3. query.txt -  set of queries  and operations alex can execute.
		4. main.py - module to fetch user query , call function to map user query to category and further execute the query
		5. preprocess.py - module to remove stopwords and perform stemming operations on the query
		6. handler.py - contains handler functions for the query based on the matched category
		7. support.py - contains helper functions for the operations
		8. web.py - module to use name entity recognizer to execute web queries
		9. duckduckgo.py   - module to use duckduckgo api to fetch results for generic queries

Python standards followed
==========================
1. Style Guide for Python Code (PEP 8):
   https://www.python.org/dev/peps/pep-0008

2. Docstring conventions (PEP 257):
    https://www.python.org/dev/peps/pep-0257/
3. Maximum Line Length
   Limit all lines to a maximum of 79 characters.


Python dependencies
===================
nltk
-----
    sudo pip install -U nltk
    http://www.nltk.org/install.html

unirest
------
sudo pip install unirest
https://github.com/Mashape/unirest-python

requests
--------
sudo pip install requests
https://pypi.python.org/pypi/requests



