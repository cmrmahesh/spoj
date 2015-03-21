for _ in xrange(int(raw_input())):
	s, p = raw_input().split()

	if p not in s:
		print 'Not Found'
	else:
		print s.count(p)
		for i in xrange(len(s)):
			if s.startswith(p, i):
				print i+1,
		print
	print
