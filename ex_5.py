src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]

#первый вариант
result = []
replays = []
for numb in src:
	indx = src.index(numb)
	if numb in src[indx + 1:] and numb not in replays:
		replays.append(numb)

for numb in src:
	if numb not in replays:
		result.append(numb)
		
print(f'replays: {replays}')
print(f'result: {result}')

#второй вариант
from collections import Counter

replays = Counter(src)
print(f'replays: {replays}')
for numb in replays:
	if replays[numb] == 1 and numb not in result:
		result.append(numb)

print(f'result: {result}')