import os


folders = {'my_prolect' : ['settings', 'mainapp', 'adminapp', 'authapp']}
for key, items in folders.items():
	if os.path.exists(key):
		print(f'папка {key} существует')
	else:
		for item in items:
			dir_ = os.path.join(key, item)
			os.makedirs(dir_)
