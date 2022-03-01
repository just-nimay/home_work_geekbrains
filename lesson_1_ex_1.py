while True:
	inp = int(input('введите число: '))
	s = inp 
	if s < 60:
		s %= 60
		print(s, 'сек')
	elif s >= 60 and s < 3600:
		s %= 3600 
		m = s // 60 
		s %= 60
		print(m, 'мин', s, 'сек')
	elif s >= 3600 and s < 86400:
		h = s // 3600 
		s %= 3600 
		m = s // 60 
		s %= 60
		print(h, 'час', m, 'мин', s, 'сек')
	elif s >= 86400:
		d = s // 86400
		s %= 86400
		h = s // 3600 
		s %= 3600 
		m = s // 60 
		s %= 60
		print(d, 'дн', h, 'час', m, 'мин', s, 'сек')
