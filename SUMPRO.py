for _ in xrange(int(raw_input())):
	n = int(raw_input())
	l = [ n / i for i in xrange(1, n + 1)]
	print sum(l[i] * (i+1) for i in xrange(len(l))) % 1000000007
