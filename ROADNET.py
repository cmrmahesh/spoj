for _ in xrange(int(raw_input())):
	n = int(raw_input())
	l = [map(int,raw_input().split()) for _ in xrange(n)]
	s = []
	for j in xrange(n):
		for i in xrange(1,n):
			if l[j][i] + l[(i+1)%n][(i+2)%n] != l[j][(i+2)%n]:
				s.append((j,i))
	print s
