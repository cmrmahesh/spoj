while True:
	try:
		n = int(raw_input())
	except Exception, e:
		break
	print 2 + (n - 2) * 2
