while True:	
	x = []
	a = raw_input()
	b = raw_input()
	for i in xrange(len(a)):
		if b.count(a[i]) != 0:
			x.append(a[i])

	x.sort()
	print ''.join(x)