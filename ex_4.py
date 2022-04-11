import os

directory = 'my_project'
file_dict = {}
files = []
max_size = 0

for p, d, f in os.walk(directory):
	for i in f:
		file_path = os.path.join(p, i)
		size = os.stat(file_path).st_size
		files.append(size)
		if size > max_size:
			max_size = size

i = 1
for j in range(len(str(max_size))):
	i *= 10
	file_dict[i] = 0

for  file in files:
	file_dict[10 ** len(str(file))] += 1

print(file_dict)



