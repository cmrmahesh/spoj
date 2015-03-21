from collections import defaultdict
while True:
	try:
		n, q = map(int, raw_input().split())
	except ValueError:
		break

	a = raw_input().split()
	for _ in xrange(q):
		c = defaultdict(int)
		i, j = map(int, raw_input().split())
		for i in xrange(i - 1, j):
			c[a[i]] += 1
		# print c
		print max(c.values())
