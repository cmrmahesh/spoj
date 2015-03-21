while True:
	a, d = map(int, raw_input().split())
	if a == 0:
		break
	ap = map(int, raw_input().split())
	dp = map(int, raw_input().split())
	mad = min(ap)
	dp.sort()
	if mad < dp[1]:
		print 'Y'
	else:
		print 'N'

