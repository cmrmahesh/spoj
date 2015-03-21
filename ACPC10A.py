while True:
	a, b ,c = map(int, raw_input().split())
	if a == b == c == 0:
		break
	if b - a == c - b:
		print 'AP %s' %(c +(c - b))
	elif b/a == c/b:
		print 'GP %s' %(c *(c/b))
