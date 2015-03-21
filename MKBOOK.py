import collections
l = 1
while True:
	a, b = map(int, raw_input().split())
	s = ""
	for i in xrange(a,b + 1):
		s += str(i)
	c = collections.Counter(s)
	#print s,c
	print 'Case %s:' %l,
	l += 1
	for i in xrange(10):
		print '%s:%s' %(i, c[str(i)]),

