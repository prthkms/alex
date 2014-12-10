import re
import os
import support
import pwd
import time

def lines(query):
	filename = support.get_file_name(query)
	with open(filename) as openfile:
		return len(openfile.readlines())

def words(query):
	filename = support.get_file_name(query)
	with open(filename) as openfile:
		return len(openfile.read().split())

def file_info(query):
	filename = support.get_file_name(query)
	stat_info = os.stat(filename)
	owner_name = pwd.getpwuid(stat_info.st_uid).pw_name
	print 'owner : '+owner_name
	file_size = support.get_readable_filesize(stat_info.st_size)
	print 'size : '+file_size
	print 'created : '+time.ctime(stat_info.st_ctime)
	print 'last modified : '+time.ctime(stat_info.st_mtime)

def make_executable(query):
	filename = support.get_file_name(query)
	os.system('chmod +x '+filename)

def search(query):
	print '''I\'m a little confused. Please enter a choice
1 : Search for file by its name
2 : Search for files with contain a keyword
'''
	try:
		choice = int(raw_input('>> '))
		if(choice == 1):
			filename = raw_input('Enter file name : ')
			os.system('locate '+filename)
		elif(choice == 2):
			keyword = raw_input('Enter keyword : ')
			print '''By default I\'ll start searching from HOME directory. But this usually takes time.
1 : Search from HOME directory
2 : Search from a custom location
'''
			location = int(raw_input('>> '))
			if(location == 1):
				os.system('grep -i -n -r \''+keyword+'\' '+os.path.expanduser('~'))
			elif(location == 2):
				directory = raw_input('Enter directory : HOME/')
				directory = os.path.join(os.path.expanduser('~'),directory)
				print directory
				if(os.path.isdir(directory)):
					os.system('grep -i -n -r \''+keyword+'\' '+directory)
				else:
					print 'Invalid directory'
					return
			else:
				print 'Invalid input'
		else:
			print 'Invalid input'
			return
	except:
		print 'Something went wrong. Most likely its an input error. Please try again'