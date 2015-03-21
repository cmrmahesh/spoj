for _ in xrange(int(raw_input())):
	_ = raw_input()
	s = raw_input().split()

	if s[1] == '+':
		t = int(s[0]) + int(s[2])
	elif s[1] == '*':
		t = int(s[0]) * int(s[2])
	elif s[1] == '-':
		t = int(s[0]) - int(s[2])
	elif s[1] == '/':
		t = int(s[0]) / int(s[2])

	if len(s) > 3:
		for i in xrange(3, len(s)-2, 2):
			if s[i] == '+':
				t = t + int(s[i + 1])
			elif s[i] == '*':
				t = t * int(s[i + 1])
			elif s[i] == '-':
				t = t - int(s[i + 1])
			elif s[i] == '/':
				t = t / int(s[i + 1])

	print t
