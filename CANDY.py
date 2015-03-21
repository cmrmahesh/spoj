while True:
	n = int(raw_input())
	if n == -1:
		break
	a = []
	s = 0
	for i in range(0,n):
		d=int(raw_input())
		s  += d
		a.append(d)
	avg = int(s/n)
	if avg*n != s:
		print -1
	else:
		r=0
		for i in range(0,n):
			if a[i]<avg:
				r += (avg - a[i])
		print r

