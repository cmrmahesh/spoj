def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

def lcm(a, b):
	return (a * b) // gcd(a, b)

def lcmm(*args):
	return reduce(lcm, args)

for _ in xrange(int(raw_input())):
	n = int(raw_input())
	print lcmm(*range(1,n)) % 1000000007


#f = lambda a,b: "f(%s,%s)" % (a,b)
#print reduce(f, "abcd")
