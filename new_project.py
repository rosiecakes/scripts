import os
import shutil
import sys

from datetime import datetime as dt

# Variable definitions
ROOT = '/Volumes/T7/Al'
FOLDER = '/' + dt.today().strftime('%Y-%m-%d')
FILENAME = '_'.join([arg for arg in sys.argv[1:]])
TEMPLATE = ROOT + '/Assets/Proj_Template.prproj'
NEW_PROJ = f"{ROOT}{FOLDER}{FOLDER}_{FILENAME}.prproj"

try:
	if not FILENAME: raise TypeError

	# Create the new folder with the date as the name
	os.mkdir(ROOT + FOLDER)
	print('\nā  New Folder Created! š\nš', ROOT + ' --> ' + FOLDER)

	# Copy the Premiere Pro Template file and rename it
	shutil.copy(TEMPLATE, NEW_PROJ)
	print('\nš„³  Started New Project! š\nš¼', NEW_PROJ)

	# Open the new project in Premiere Pro and Finder
	# os.system(f'open {NEW_PROJ}')
	os.system(f'open {ROOT + FOLDER}')

except TypeError:
	print('\nā ļø  Please enter a project keyword')

except OSError as e:
	print('\nā Could not create new folder\n', e)
