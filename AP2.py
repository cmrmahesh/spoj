for _ in xrange(int(raw_input())):
	t, tl, s = map(int, raw_input().split())
	n = 2 * s / (t + tl)
	d = (2 * t- 2*s/n)/(5-n)
	a = t - 2 * d
	print n
	print ' '.join([str(a+ti*d) for ti in xrange(n)])
