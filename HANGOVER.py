while True:
	c = float(raw_input())
	if c == 0.00:
		break
	no = 0
	leca = 0
	i = 2
	while leca <= c:
		leca += 1.0 / i
		i += 1
		no += 1
	print no,'card(s)'
