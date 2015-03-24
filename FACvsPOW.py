from math import factorial
for _ in xrange(int(raw_input())):
	a = int(raw_input())
	i = a * 2
	while True:
		if factorial(i) > a ** i:
			print i
			break
		i += 1

