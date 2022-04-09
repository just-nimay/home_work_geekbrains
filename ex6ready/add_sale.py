import sys

count = True
inp = sys.argv
if len(inp) == 1:
		with open('bakery.csv') as f:
			f.seek(0)
			print(f.read())
else:
	for i, item in enumerate(inp):
		if i == 0:
			continue

		elif len(inp[i]) == 1 and len(inp) <= 2:
			n = int(item)
			with open('bakery.csv') as f:
				lines = f.readlines()
				for i, item in enumerate(lines):
					if i == n:
						print(item, end='')

		elif len(item) > 1 and i != 0:
			with open('bakery.csv', 'a') as f:
				f.write(item + '\n')

		elif count == True and len(inp[i]) == 1 and len(inp[i + 1]) == 1 and len(inp) > 2:
			n_1 = int(inp[i])
			n_2 = int(inp[i + 1])
			count = False
			with open('bakery.csv') as f:
				lines = f.readlines()
				for i, item in enumerate(lines):
					if i >= n_1 and i <= n_2:
						print(item, end='')


			