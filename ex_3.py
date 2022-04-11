
import os
import shutil 

tamp_dir = 'templates'
if not os.path.exists(tamp_dir):
	os.mkdir(tamp_dir)

directory = r'my_project'
files = []

for r, d, f in os.walk(directory):
	for i in f:
		if '.html' in i:
			files.append(os.path.join(r, i))
for path in files:
	new_folder = os.path.join(tamp_dir, os.path.basename(os.path.dirname(path)))
	if not os.path.exists(new_folder):
		os.mkdir(new_folder)
	save_path = os.path.join(new_folder, os.path.basename(path))
	shutil.copy(path, save_path)
'''
import os
import shutil
my_dir = 'task3'  # save folder
if not os.path.exists(my_dir):
    os.mkdir(my_dir)

folder = r'my_project'  # search folder
files = []


for r, d, f in os.walk(folder):
    for file in f:
        if '.html' in file:
            files.append(os.path.join(r, file))
for path in files:
    folder_new = os.path.join(my_dir, os.path.basename(os.path.dirname(path)))
    if not os.path.exists(folder_new):
        os.mkdir(folder_new)
    save_path = os.path.join(folder_new, os.path.basename(path))
    shutil.copy(path, save_path)
    '''