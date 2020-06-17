import os
import sys
import time
from zipfile import ZipFile

if not len(sys.argv) > 1:
	exit()

cwd = os.getcwd()
folders = sys.argv[1:len(sys.argv)]

def zip_process_dir(zipfile, dirname):
	for folderName, subfolders, filenames in os.walk(dirname):
		for filename in filenames:
			filepath = os.path.join(folderName, filename)
			if not os.path.isfile(filepath):
				zip_process_dir(zipfile, filepath)
			else:
				zippath = filepath.replace(dirname, '')
				zipfile.write(filepath, zippath)

def zip(folder, zipfile_path):
	with ZipFile(zipfile_path, 'w') as zipfile:
		if not os.path.isfile(folder):
			zip_process_dir(zipfile, folder)
		else:
			#filename = os.path.join(cwd, )
			zipfile.write(folder, os.path.basename(folder))

def unzip(folder, zipfile_path):
	with ZipFile(folder, 'r') as zipfile:
		zipfile.extractall(path=folder.replace('.zip', ''))

for f in folders:
	zipfile_path = os.path.join(cwd, os.path.basename(f).split('.')[0] + '.zip')
	if '.zip' in f:
		unzip(f, z)
	else:
		zip(f, z)

#print(folders)
input('Finished.. Press enter to exit!')
