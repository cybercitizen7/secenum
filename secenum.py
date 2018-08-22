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
	# Store all the current running Windows Processes  in a List
	win_processes = c.Win32_Process()
	# Open the file containing all security apps vendors
	with open( filepath, newline='' ) as csv_file:
		# Returns reader object that supports iterator protocol
		parsed_app_names = csv.DictReader(csv_file)
		# Iterate over every app name in our reader object
		for app_name in parsed_app_names:
			# Iterate over all processes in Windows
			for process in win_processes:
				# If one of the processes matches the security vendor]
				if process.Name == app_name['process_name']:
					# Append it to our list, since it is run on user machine
					used_secapps_list.append(app_name['vendor'])

def print_used_secapps():
	# Convert list into a set, to get rid of duplicated entries
	s = set(used_secapps_list)

	count = 1
	# Loop through all sec apps running on computer and print them out
	for secapp in s:
		print ('#{0} {1}'.format(count, secapp))
		count += 1



retrieve_used_secapps('secapps.csv')
print_used_secapps()

