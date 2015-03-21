def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

for _ in xrange(int(raw_input())):
	a, b = map(int, raw_input().split())
	print gcd(a, b)
