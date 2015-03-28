while True:
	g, b = map(int, raw_input().split())
	if g == -1:
		break
	print (g + b) / (min(g, b)+1)
