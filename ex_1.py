'''
Не используя библиотеки для парсинга, распарсить 
(получить определённые данные) файл логов web-сервера 
nginx_logs.txt
'''

def parse(content):
	words = line.split(' ')
	ip = words[0]
	get = words[5]
	get = get[1:]
	link = words[6]
	tuple_ = (ip, get, link)
	return tuple_


ready_list = []
with open('nginx_logs.txt') as f:
	for line in f:
		ready_content = parse(line)
		ready_list.append(ready_content)

for i in ready_list:
	print(i)



