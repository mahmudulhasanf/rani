version="2.3.6"
#IMPORT
import getpass,time,os,sys
import signal
import time,os,sys
import sys, random
import threading,time
#CVALUE
blue= '\33[94m'
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
cyan  = "\033[96m"
end = '\033[0m'
black="\033[0;30m"
line=yellow+"======================================================================================================================"+end
space=" "
logo=blue+str(""" ___       _____     _   _     _              
(  _`\    (  _  )   ( ) ( )   (_)   /'\_/`\   
| (_(_)   | (_) |   | |_| |   | |   |     |   
|  _)     |  _  |   |  _  |   | |   | (_) |   
| |       | | | |   | | | |   | |   | | | |   
(_)       (_) (_)   (_) (_)   (_)   (_) (_)   
                                              
                                              """)+end

notice=""
def header():
	print(logo+cyan+"\n\n\n\t\tDeveloped By : Mahmudul Hasan Fahim \n\n"+green+"\t\t     Version : "+str(version)+" \n\n"+end+line+"\n"+end)
def clear():
        os.system("clear || cls")
count=1
erase = '\x1b[1A\x1b[2K'
count=1
about=12

os.system("clear")
header()
print(cyan+"\n\t\t[•] Checking For Updates")
time.sleep(0.7)


try:
	import requests
except:
	os.system("pip install requests")
import requests
r=requests.get('https://pastebin.com/raw/0e7CzUNG')
upchck=r.text
if upchck==version:
	pass
elif upchck!=version:
	os.system("clear")
	header()
	print(cyan+"\n  [°] Installing The Updated Tools. Allow Up to 10 minutes ")
	time.sleep(2)
	os.system("clear")
	notice=cyan+"\t\t[°] Installing Updated Tools.. \n"
	header()
	notice=""
	print("\n")
	clear()
	notice=cyan+"\t\t[•] Backing up the ROC-X...."
	header()
	os.system("mkdir /data/data/com.termux/files/usr/bin/roc-x_updater")
	os.system("cp -rf /data/data/com.termux/files/usr/bin/roc-x /data/data/com.termux/files/usr/bin/roc-x_updater")
	try:
		clear()
		notice=cyan+"\t\t[•] Updating the Tools...."
		header()
		os.system("cd /data/data/com.termux/files/usr/bin")
		os.system("cd /data/data/com.termux/files/usr/bin && rm -rf roc-x")
		print(green)
		os.system("cd /data/data/com.termux/files/usr/bin && git clone https://github.com/RootOfCyber/roc-x")
		
		clear()
		notice=green+"\t\t[√] Update Successful!"
		header()
		#os.kill(os.getppid(), signal.SIGHUP)
		os.system("rm -rf /data/data/com.termux/files/usr/bin/roc-x_updater")
		for i in range(99999999999):
			r2=requests.get("https://pastebin.com/raw/6sBnXFV7")
			r=requests.get('https://pastebin.com/raw/0e7CzUNG')
			upchck=r.text

			os.system("clear")
			print(green+"\n"*4+"\t  [✓]  Successfully Updated to ROC-X "+yellow+str(upchck)+green+" !\n\n\n\n"+cyan+"  [•] What's New in Version "+str(upchck)+" ?\n\n")
			rng=r2.text
			exec(rng)
			print(yellow+"\n\n\n [•••] TerMux Restart is Required for The Update. Please Restart Termux For The ROC-X Updated Version")
			a=input()

	except:
		clear()
		notice=red+"\t\t[×] Update Failed!"
		header()
		sjsjstshsb=input(cyan+"\n\n\t     Press Enter to Restore ROC-X")
		os.system("cd /data/data/com.termux/files/usr/bin")
		os.system("cd /data/data/com.termux/files/usr/bin && mkdir roc-x")
		os.system("cd /data/data/com.termux/files/usr/bin && cp -rf /data/data/com.termux/files/usr/bin/roc-x_updater/roc-x /data/data/com.termux/files/usr/bin")
		os.system("rm -rf /data/data/com.termux/files/usr/bin/roc-x_updater")
		for i in range(99999999999):
			os.system("clear")
			a=input(cyan+"\n"*10+" [>] Please Exit Termux from Notification Bar. Then Again Open ROC-X Tools By :\n\n "+yellow+"\t [1] Exit Termux\n\t [2] Open Termux"+"\n\t [3] command : rocx")
		
		
