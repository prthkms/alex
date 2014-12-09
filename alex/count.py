import re
import os

def lines(query):
	match = re.search(r'\S*\.[\d\w]{1,4}', query)
	if(match):
		filename = match.group()
		if(os.path.isfile(filename)):
			content = open(filename).readlines()
			print len(content)
			return
		else:
			start = match.start()
			end = match.end()
			spaces = re.finditer(r' ', query)
			space_index = []
			for space in spaces:
				space_index.append(space.start())
			space_index.pop()
			for i in space_index:
				filename = query[i+1:end]
				if(os.path.isfile(filename)):
					content = open(filename).readlines()
					print len(content)
					return
			print 'Unable to locate file'

def words(query):
	match = re.search(r'\S*\.[\d\w]{1,4}', query)
	if(match):
		filename = match.group()
		if(os.path.isfile(filename)):
			content = open(filename).read().split()
			print len(content)
			return
		else:
			start = match.start()
			end = match.end()
			spaces = re.finditer(r' ', query)
			space_index = []
			for space in spaces:
				space_index.append(space.start())
			space_index.pop()
			for i in space_index:
				filename = query[i+1:end]
				if(os.path.isfile(filename)):
					content = open(filename).read().split()
					print len(content)
					return
			print 'Unable to locate file'