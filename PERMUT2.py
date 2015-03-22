while True:
	n = int(raw_input())
	if n == 0:
		break
	a = map(int, raw_input().split())
	k = 1
	per = [0] * n
	for x in a:
		per[x - 1] = k
		k += 1
	if per == a:
		print 'ambiguous'
	else:
		print 'not ambiguous'
