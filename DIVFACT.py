import math

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

def factors(n):
    return set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def main():
	for _ in xrange(int(raw_input())):
		n = int(raw_input())
		k = fact(n)
		#su = 0
		#print k
		#for i in xrange(1, int(math.sqrt(k)) + 1):
		#	if k % i == 0:
		#		su += 2
		#if i * i == k:
		#	su += 1
		print len(factors(k)) % 1000000007

main()
