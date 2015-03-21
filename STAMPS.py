for t in xrange(1,int(raw_input())+1):
	tk, f = map(int, raw_input().split())
	l = map(int, raw_input().split())
	l.sort()
	l.reverse()
	c = 0
	sum = 0
	for i in xrange(len(l)):
		if sum >= tk:
			break
		else:
			sum += l[i]
			c += 1
	if sum >= tk:
		print 'Scenario #%s:' %(t)
		print c
		print
	else:
		print 'Scenario #%s:' %(t)
		print 'impossible'
		print
