for _ in xrange(int(raw_input())):
	raw_input()
	a, _, b, _, c = raw_input().split()
	if 'm' in a:
		a = int(c) - int(b)
	elif 'm' in b:
		b = int(c) - int(a)
	else:
		c = int(a) + int(b)
	print '%s + %s = %s' % (a, b, c)
