import math

def factors(n):
	fact=[1,n]
	check=2
	rootn=math.sqrt(n)
	while check<rootn:
		if n%check==0:
			fact.append(check)
			fact.append(n/check)
		check+=1
	if rootn==check:
		fact.append(check)
		# fact.sort()
	return len(fact)

def main():
	for _ in xrange(int(raw_input())):
		n = int(raw_input())
		k = math.factorial(n)
		print factors(k) % 1000000007

main()
