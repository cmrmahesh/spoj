for _ in xrange(int(raw_input())):
	n = int(raw_input())
	if n & 1 == 0:
		print int(bin(n)[-1:1:-1], 2)
	else:
		print n
