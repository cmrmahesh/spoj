from sys import stdout

while True:
	t = int(raw_input())
	if t == 0:
		break
	s = raw_input()
	l = []
	k = 0
	while k < len(s):
		l.append(s[k : k + t])
		k = k + t
	
	for i in xrange(len(l)):
		if i % 2 != 0:
			l[i] = l[i][::-1]

	for i in xrange(t):
		for j in xrange(len(l)):
			x = l[j]
			stdout.write(x[i])
	stdout.write('\n')	