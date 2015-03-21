print 'Ready'
while True:
	k = raw_input()
	s = set(k)
	if ' ' in s:
		break
	elif (('p' in s) and ('q' in s)) or (('d' in s) and ('b' in s)):
		print 'Mirrored pair'
	else:
		print 'Ordinary pair'
