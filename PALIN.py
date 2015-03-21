for _ in xrange(int(raw_input())):
	i = int(raw_input()) + 1

	while True:
		
		if int(str(i)[::-1]) == i:
			print i
			break

		i += 1

