for _ in xrange(int(raw_input())):
	a = raw_input()
	b = raw_input()
	al = len(a)
	bl = len(b)
	if al < bl:
		c = bl - al
	else:
		c = al - bl

	for i in xrange(al):
		if a[i] != b[i]:
			c += 1
	print c
