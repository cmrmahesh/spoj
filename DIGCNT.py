from collections import defaultdict
while True:
	a, b = map(int, raw_input().split())
	if a == b == 0:
		break
	c = {'1' : 0, '2' : 0, '3' : 0, '4' : 0, '5' : 0, '6' : 0, '7' : 0, '8' : 0, '9' : 0}
	s =""
	for i in xrange(a, b+1):
		s = ''.join(str(i))
	for x in s:
		c[x] += 1
	print ' '.join(c.values())
