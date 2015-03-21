for _ in xrange(int(raw_input())):
	n = int(raw_input())
	odds = 2 ** bin(n).count('1')
	print n+1-odds, odds
