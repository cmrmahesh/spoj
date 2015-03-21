while True:
	try:
		n = int(raw_input()) - 1
	except Exception, e:
		break
	print (n << 1 if n else 1)
