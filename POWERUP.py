while True:
	a, b, c = map(int, raw_input().split())
	if a == b == c == -1:
		break
	print pow(a, pow(b, c), 1000000007)
