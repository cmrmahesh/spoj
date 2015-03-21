l = map(int, raw_input().split())
c = 0
for i in xrange(l[0], l[1] + 1):
	dc = 1
	for j in xrange(1, i / 2 + 1):
		if i % j == 0:
			dc += 1

	if dc == l[2]:
		c += 1

print c