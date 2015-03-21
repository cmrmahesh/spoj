for _ in xrange(int(raw_input())):

	m = map(int, raw_input().split())
	n = map(int, raw_input().split())

	mdif = abs(m[1] - n[1])

	for i in xrange(1,len(m)):
		if m[i] in n[1:]:
			mdif = 0
			break
		else:
			for j in xrange(1,len(n)):
				if abs(m[i] - n[j]) < mdif:
					mdif = abs(m[i] - n[j])

	print mdif
