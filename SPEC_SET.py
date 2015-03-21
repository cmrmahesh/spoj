for _ in xrange(int(raw_input())):
	n, k = map(int, raw_input().split())
	s = set()
	for i in xrange(1, n+1):
		if i*k not in s:
			s.add(i)
	print s
