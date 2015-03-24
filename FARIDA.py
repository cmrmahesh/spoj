t = int(raw_input()) + 1
for j in xrange(1,t):
	n = int(raw_input())
	a = map(int, raw_input().split())
	if n == 1:
		print 'Case {}: {}'.format(j,a[0])
	else:
		c = a[0]
		d = a[1]
		for i in xrange(2,n,2):
			c += a[i]
		for i in xrange(3,n,2):
			d += a[i]
		print 'Case {}: {}'.format(j,c if c > d else d)
