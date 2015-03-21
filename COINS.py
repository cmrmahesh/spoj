d = {}

def max_byteland(n):
	if n==0:
		return 0
	else:
		if n in d:
			r = d[n]
		else:
			r = max(n, max_byteland(n/2)+max_byteland(n/3)+max_byteland(n/4))
			d[n] = r
		return r

for _ in xrange(10):
	n = int(raw_input())
	print max_byteland(n)
	d.clear()
