while True:
	s = raw_input()
	dp = [1]
	for i in xrange(1,len(s)):
		if int(s[i-1])*10 + int(s[i]) < 27:
			dp[i] = dp[i-1] + 1
		else:
			dp[i] = dp[i-1]
	print sum(dp)

