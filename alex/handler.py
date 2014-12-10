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