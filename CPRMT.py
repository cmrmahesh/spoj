from sys import stdin
#stdin = open('test.txt', 'r')
lines = iter(stdin.read().split())
for a in lines:
	b = set(lines.next())
	x = [i for i in a if i in b]
	print ''.join(sorted(x))
