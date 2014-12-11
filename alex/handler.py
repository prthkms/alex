import re
import os
import support
import pwd
import time
import subprocess

def lines(query):
	filename = support.get_file_name(query)
	if(os.path.isfile(filename)):
		with open(filename) as openfile:
			print len(openfile.readlines())
	else:
		print 'File not found : '+filename

def words(query):
	filename = support.get_file_name(query)
	if(os.path.isfile(filename)):
		with open(filename) as openfile:
			print len(openfile.read().split())
	else:
		print 'File not found : '+filename

def file_info(query):
	filename = support.get_file_name(query)
	if(os.path.isfile(filename)):
		stat_info = os.stat(filename)
		owner_name = pwd.getpwuid(stat_info.st_uid).pw_name
		print 'owner : '+owner_name
		file_size = support.get_readable_filesize(stat_info.st_size)
		print 'size : '+file_size
		print 'created : '+time.ctime(stat_info.st_ctime)
		print 'last modified : '+time.ctime(stat_info.st_mtime)
	else:
		print 'file not found'

def make_executable(query):
	filename = support.get_file_name(query)
	if(os.path.isfile(filename)):
		os.system('chmod +x '+filename)
	else:
		print 'file not found'

def search(query):
	print '''I\'m a little confused. Please enter a choice
1 : Search for file by its name
2 : Search for files which contain a keyword
'''
	try:
		choice = int(raw_input('>> '))
		if(choice == 1):
			filename = support.get_file_name(query)
			if(filename):
				os.system('locate -b \'\\'+filename+'\'')
			else:
				print 'not able to get the filename'
		elif(choice == 2):
			keyword = raw_input('Enter keyword : ')
			print '''By default I\'ll start searching from HOME directory. But this usually takes time.
1 : Search from HOME directory
2 : Search from current directory
'''
			location = int(raw_input('>> '))
			if(location == 1):
				os.system('grep -i -n -r \''+keyword+'\' '+os.path.expanduser('~'))
			elif(location == 2):
				os.system('grep -i -n -r \''+keyword+'\' '+os.path.abspath(os.curdir))
			else:
				print 'Invalid input'
		else:
			print 'Invalid input'
			return
	except:
		print 'Something went wrong. Most likely its an input error. Please try again'

def search_new(query):
	print '''I\'m a little confused. Please enter a choice
1 : Search for file by its name
2 : Search for files which contain a keyword
'''
	try:
		choice = int(raw_input('>> '))
		if(choice == 1):
			filename = support.get_file_name(query)
			if(filename):
				os.system('locate -b \'\\'+filename+'\'')
			else:
				print 'not able to get the filename'
		elif(choice == 2):
			keyword = raw_input('Enter keyword : ')
			if(len(keyword) > 0):
				os.system('grep -i -n -r \''+keyword+'\' '+os.path.abspath(os.curdir))
			else:
				print 'Invalid input'
		else:
			print 'Invalid input'
			return
	except:
		print 'Something went wrong. Most likely its an input error. Please try again'

def add_to_path(query):
	new_entry = support.get_path(query)
	if(new_entry):
		print 'Adding '+new_entry+' to PATH variable.'
		print '''1 : confirm
2 : cancel
	'''
		choice = int(raw_input('>> '))
		if(choice == 1):
			home_dir = os.path.expanduser('~')
			bashrc = open(os.path.join(home_dir, ".bashrc"), "a")
			bashrc.write('\n\nexport PATH=\"'+new_entry+':$PATH\"\n')
			bashrc.close()
			os.system('source '+os.path.join(os.path.expanduser('~'),'.bashrc'))
			print 'Success!!'
			print os.system('echo $PATH')
	else:
		print 'We were unable to extract the \'path\' from your query.'

def system_info(query):
	proc = subprocess.Popen(["uname -o"], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	print "operating system : "+str(out),

	proc = subprocess.Popen(["uname"], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	print "kernel : "+str(out),

	proc = subprocess.Popen(["uname -r"], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	print "kernel release : "+str(out),

	proc = subprocess.Popen(["uname -m"], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	print "architecture : "+str(out),

	proc = subprocess.Popen(["uname -n"], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	print "network node name : "+str(out),