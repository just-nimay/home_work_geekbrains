import requests
import sys
import datetime

def currency_rates(cur):
	cur = str(cur)
	response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
	response = response.text
	x = response.replace('<', ' ')
	x = x.replace('>', ' ')
	x = x.replace('/', '')
	z = x.split(' ')

	indx = 0
	value = None
	for i in z:
		if 'Date' in i:
			date = i[6:-1]
		if i == cur:
			indx = z.index(i)
			value = z[indx + 13]
			value = value[:-2]

	date = date.replace('.', '')
	date = datetime.datetime.strptime(date, '%d%m%Y').date()
	
	return date, value

	if __name__ == '__main__':
		print('модуль запущен не импортируясьpytho')