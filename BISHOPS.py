import sys
for num in sys.stdin.readlines() :
	x = int(num)
	if x == 1 :
		print 1
	else :
		print 2 * (x - 1)
