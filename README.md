
Alex
=====

###Description
---------------
Alex is an open source Natural Language Processing based command line access tool.

###Installation
----------------

1. To install alex, run the following in your terminal

  ```bash
  git clone https://github.com/pratheekms/alex
  ```

2. Then navigate to alex directory and run setup

  ```bash
  python setup.py
  ```

###Python dependencies
----------------------
1. [nltk](http://www.nltk.org/install.html)
  ```bash
  sudo pip install -U nltk
  ```

2. [unirest](https://github.com/Mashape/unirest-python)
  ```bash 
  sudo pip install unirest
  ```
    
3. [requests](https://pypi.python.org/pypi/requests)
  ```bash 
  sudo pip install requests
  ```

###Modules
----------
Alex contains the following files (modules):

1. README - This readme file.

2. setup.py - contains code to copy files and install alex to your home or a custom directory.

3. LICENSE - GNU GENERAL PUBLIC LICENSE

4. alex - subdirectory containing files to process queries and perform operations.
  Within alex 
	* corpus.txt - contains corpus of queries in different forms for alex. 
	* category.txt - contains list of categories the processed queries can be mapped to (eg. count lines, file info etc).
	* query.txt -  set of queries  and operations alex can execute.
	* main.py - module to fetch user query, calls function to map user query to category and further execute the query.
	* preprocess.py - module to remove stopwords and perform stemming operations on the query.
	* handler.py - contains handler functions for the query based on the matched category.
	* support.py - contains helper functions for the operations.
	* web.py - module to use named entity recognizer(NER) to execute web queries.
	* duckduckgo.py  - module to use duckduckgo api to fetch results for generic queries.

###Example queries
------------------

```bash
alex locate filename
>By default I\'ll start searching from HOME directory. 
>But this usually takes time.
>1 : Search from HOME directory
>2 : Search from a custom location
1
```

```bash
alex find number of words in corpus.txt
```

```bash
alex find the file index.php
>I\'m a little confused. Please enter a choice
>1 : Search for file by its name
>2 : Search for files with contain a keyword
1
```
```bash
alex find the file with apple
>I\'m a little confused. Please enter a choice
>1 : Search for file by its name
>2 : Search for files with contain a keyword
2
>Enter keyword : apple
```
```bash
alex get me file info of index.php
```

```bash
alex what is the weather in london?
```

```bash
alex who is Abraham Lincoln
```

```bash
alex give me the system information
```

```bash
alex how many lines are there in corpus.txt?
```

```bash
alex make main.py executable
```

```bash
alex add  /aost/project to path
>1 : confirm
>2 : cancel
1
```


###Python standards followed
----------------------------
1. [Style Guide for Python Code (PEP 8)](https://www.python.org/dev/peps/pep-0008)
   

2. [Docstring conventions (PEP 257)](https://www.python.org/dev/peps/pep-0257/)
    
3. Maximum Line Length
   Limit all lines to a maximum of 79 characters.



    



