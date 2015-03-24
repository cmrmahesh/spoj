def s(n, m):
	if n == 0 or m == 0:
		return 0
	elif n == 0 and m == 0:
		return 1
	else:
		return m * s(n-1, m) + s(n-1, m-1)



for _ in xrange(int(raw_input())):
	n, m = map(int, raw_input().split())
	print s(n, m) % 2
