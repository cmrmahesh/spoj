for _ in xrange(int(raw_input())):
	l = map(int , raw_input().split())
        
	l[0] = int(str(l[0])[::-1])
	l[1] = int(str(l[1])[::-1])

	sum = l[0] + l[1]

	sum = int(str(sum)[::-1])

	print sum

	

