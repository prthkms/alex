import handler
import web
import re
import os

def assign_handler(query, category):
	if(category == 'count lines'):
		handler.lines(query)
	elif(category == 'count words'):
		handler.words(query)
	elif(category == 'weather'):
		web.weather(query)
	elif(category == 'no match'):
		web.generic(query)
	elif(category == 'file info'):
		handler.file_info(query)
	elif(category == 'executable'):
		handler.make_executable(query)

def get_file_name(query):
	match = re.search(r'\S*\.[\d\w]{1,4}', query)
	if(match):
		filename = match.group()
		if(os.path.isfile(filename)):
			return filename
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
					return filename
			print 'Unable to locate file'

def get_readable_filesize(size):
	if(size < 1024):
		return str(size)+' bytes'
	temp = size/1024.0
	level = 1
	while(temp >= 1024 and level< 3):
		temp = temp/1024
		level += 1
	if(level == 1):
		return str(round(temp,2))+' KB'
	elif(level == 2):
		return str(round(temp,2))+' MB'
	else:
		return str(round(temp,2))+' GB'