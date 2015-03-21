f = []
fof = set()
for _ in xrange(int(raw_input())):
	i = raw_input().split()
	f.append(i[0])
	fof.update(set(i[2:]))
print len(fof.difference(set(f)))
