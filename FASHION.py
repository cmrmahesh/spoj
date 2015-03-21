for _ in xrange(int(raw_input())):
	n =  int(raw_input())
	m = map(int, raw_input().split())
	f = map(int, raw_input().split())
	m.sort()
	f.sort()
	sum = 0
	for i in xrange(n):
		sum += m[i] * f[i]

	print sum

