from math import sqrt

def find_fraction(n):
	d = int(-1 + sqrt(1 + 8*n))/2
	e = int(n - d*(d+1)/2)
	if e<= 1:
		v1,v2 = d + e,1
	else:
		v1,v2 = d-e+2,e
	if d % 2 == 0:
		string = str(v1) + '/'+ str(v2)
	else:
		string = str(v2) + '/'+ str(v1)
	return string

for _ in xrange(int(raw_input())):
	n = int(raw_input())
	ans = find_fraction(n)
	print "TERM " + str(n) + " IS " + ans
