from collections import defaultdict
n, q = map(int, raw_input().split())
a = raw_input().split()
for _ in xrange(q):
	c = defaultdict(int)
	i, j = map(int, raw_input().split())
	for i in xrange(i, j+1):
		c[a[i]] += 1
	# print c
	print max(c.values())
