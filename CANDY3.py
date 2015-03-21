for _ in xrange(int(raw_input())):
	_ = raw_input()
	n = int(raw_input())
	l =[]
	for _ in xrange(n):
		l.append(int(raw_input()))
	print

	if sum(l) % n == 0:
		print 'YES'
	else:
		print 'NO'


