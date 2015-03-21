import math
while True:
	n = int(raw_input())
	print '1',
	while n % 2 == 0:
		print 'x 2',
		n /= 2

	for i in xrange(3,int(math.sqrt(n)),2):
		while n % i == 0:
			print 'x %s' %i ,
			n /= i

	if n > 2:
		print 'x %s' %n,

	print

