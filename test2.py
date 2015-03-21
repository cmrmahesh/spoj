l = [[1112],[1912],[1892],[1234]]
for i in xrange(1, 4):
	for j in xrange(1, 3):
		if int(l[i][j-1]) < int(l[i][j]) > int(l[i][j+1]):
			l[i,j] = 'X'

print l
