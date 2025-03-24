import os
import shutil

directory = 'D:\World of Warcraft\_classic_\Screenshots'
sorted_directory = 'D:\World of Warcraft\_classic_\Sorted Screenshots'

for filename in os.listdir(directory):
	try:
		split_filename = filename.split('_')[1].split('.')[0]
		last_character = split_filename[5]
		source_directory = directory + '\\' + filename
		destiny_directory = sorted_directory + '\\202' + last_character + '\\' + filename
		# Destiny directory has to exist
		shutil.move(source_directory, destiny_directory)
	except:
		pass

