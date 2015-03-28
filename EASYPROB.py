def yoba(num):
	s, bit = [], 0
	if num == 0:
		return "0"
	while num != 0:
		if num & 1 != 0:
			if bit != 1:
				s.append("2({})".format(yoba(bit)))
			else:
				s.append("2")
		num, bit = num >> 1, bit + 1
	return "+".join(reversed(s))

for num in (137, 1315, 73, 136, 255, 1384, 16385):
	print("{}={}".format(num, yoba(num)))
