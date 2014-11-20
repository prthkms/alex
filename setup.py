import os
import stat
import sys
import shutil

def install_home_dir():
	home_dir = os.path.expanduser('~')
	install_dir = os.path.join(home_dir,'alex')
	if(os.path.exists(install_dir)):
		print 'Alex already exists !! If its a failed installation, please remove it completely to try again'
		sys.exit()
	else:
		print "Copying files . . ."
		shutil.copytree(os.path.join(os.curdir,'alex'), install_dir)
		if(os.path.exists(os.path.join(install_dir, 'main.py'))):
			print "Done."
		else:
			print "Copy failed. Exiting . . ."
			sys.exit()
		main_path = os.path.join(install_dir, 'main.py')
		st = os.stat(main_path)
		os.chmod(main_path,st.st_mode | stat.S_IEXEC) #main.py made executable	
		
		print "Adding alias to bashrc . . ."
		bashrc = open(os.path.join(home_dir, ".bashrc"), "a")
		bashrc.write("\n### Added by alex\n")
		bashrc.write("alias alex=\'"+os.path.join(install_dir, 'main.py')+"\'")
		bashrc.write("\n")
		bashrc.close()
		os.system("source ~/.bashrc")
		print "Done. You can now run alex from command line."


def install_custom_dir():
	custom_dir = raw_input("Enter the path where you would like to install alex.\n")
	custom_dir = os.path.abspath(custom_dir)
	install_dir = os.path.join(custom_dir, 'alex')
	home_dir = os.path.expanduser('~')
	if(not os.path.exists(custom_dir)):
		print "Invalid directory. Failed to install."
		sys.exit()
	elif(os.path.exists(install_dir)):
		print "Alex already exists !! If its a failed installation, please remove it completely to try again"
		sys.exit()
	else:
		print "Copying files . . ."
		shutil.copytree(os.path.join(os.curdir,'alex'), install_dir)
		if(os.path.exists(os.path.join(install_dir, 'main.py'))):
			print "Done."
		else:
			print "Copy failed. Exiting . . ."
			sys.exit()
		main_path = os.path.join(install_dir, 'main.py')
		st = os.stat(main_path)
		os.chmod(main_path,st.st_mode | stat.S_IEXEC) #main.py made executable	
		print "Adding alias to bashrc . . ."
		bashrc = open(os.path.join(home_dir, ".bashrc"), "a")
		bashrc.write("\n### Added by alex\n")
		bashrc.write("alias alex=\'"+os.path.join(install_dir, 'main.py')+"\'")
		bashrc.write("\n")	
		bashrc.close()
		os.system("source ~/.bashrc")
		print "Done. You can now run alex from command line."		

install_in_home_dir = raw_input("Alex will be installed to your home directory(~/alex) by default. Enter yes if you wish to \
proceed. Enter no to specify a custom directory. (y/n) ")

if(install_in_home_dir.lower() == 'y' or install_in_home_dir.lower() == 'yes'):
	install_home_dir()
elif(install_in_home_dir.lower() == 'n' or install_in_home_dir.lower() == 'no'):
	install_custom_dir()
else:
	print ("Sorry invalid input.\nExiting setup now . . .")
