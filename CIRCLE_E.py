from math import sqrt
for _ in xrange(int(raw_input())):
	a, b, c = map(float, raw_input().split())
	k = 1/a + 1/b + 1/c + 2*sqrt((a+b+c)/(a*b*c))
	print '{0:f}'.format(1/k)
