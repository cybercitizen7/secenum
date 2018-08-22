# ENUMERATE SECURITY / MONITORING APPS
import subprocess
import sys
import csv

try:
	import wmi
except ImportError:
	print ("Attempting to install required modeule: WMI\n")
    # Forcing python module installation
	subprocess.call([sys.executable, "-m", "pip", "install", "wmi"])
	import wmi

# Define variables
c = wmi.WMI()
used_secapps_list = []
win_processes = []

def retrieve_used_secapps( filepath ):
	print("STARTING THE TOOL\n")
	print("[WIN_PROC] Retrieving currently running windows processes ...")
	# Store all the current running Windows Processes  in a List
	win_processes = c.Win32_Process()
	print("[WIN_PROC] Found [{0}] processes!".format(len(win_processes)))
	print("\n[FILE] Reading CSV file ...")
	# Open the file containing all security apps vendors
	with open( filepath, newline='' ) as csv_file:
		# Returns reader object that supports iterator protocol
		print("[FILE] Parsing CSV file ...")
		parsed_app_names = csv.DictReader(csv_file)
		# Iterate over every app name in our reader object
		print("[ANALYSIS] Looking for security / monitoring apps on your machine ...")
		for app_name in parsed_app_names:
			# Iterate over all processes in Windows
			for process in win_processes:
				# If one of the processes matches the security vendor]
				if process.Name.lower() == app_name['process_name']:
					# Append it to our list, since it is run on user machine
					used_secapps_list.append(app_name['vendor'])

def print_used_secapps():
	# Convert list into a set, to get rid of duplicated entries
	print("[ANALYSIS] Removing any duplicate entries ...")
	s = set(used_secapps_list)
	print("\nLIST OF USED SECURITY / MONITORING APPS:")
	print("-------------------------------------------")
	# Variable used for increment count of used sec apps
	count = 1
	# Loop through all sec apps running on computer and print them out
	for secapp in s:
		print ('#{0} {1}'.format(count, secapp))
		count += 1


print("""
	   _____           ______                       
  / ____|         |  ____|                      
 | (___   ___  ___| |__   _ __  _   _ _ __ ___  
  \___ \ / _ \/ __|  __| | '_ \| | | | '_ ` _ \ 
  ____) |  __/ (__| |____| | | | |_| | | | | | |
 |_____/ \___|\___|______|_| |_|\__,_|_| |_| |_|

 ------------------- SecEnum version v1.0.0 -------------------

Created by: David "darkw1z" Kasabji
Twitter: @darkw1z
Date Created: 22.08.2018

This is an OpenSource project for enumerating security and monitoring tools used on Windows machine.
Feel free to contribute to the secapps.csv file with additional entries.
If you intend to use this tool in presentations / demonstrations, please include the developers information.

DISCLAIMER: Please do not use this tool for any illegal activities.
-------------------------------------------
	""")
retrieve_used_secapps('secapps.csv')
print_used_secapps()

