import sys
import math
s = sys.stdin.readline()
m, n = eval(s[s.find('('):-2])
s2 = sys.stdin.readline()
p, q = eval(s2[s2.find('('):-2])
print 'The salesman has traveled a total of {0:.3f} kilometers.'.format(math.sqrt((m-p)**2 + (n-q)**2))
for line  in sys.stdin.readlines():
	a, b = eval(s[s.find('('):-2])
	print 'The salesman has traveled a total of {0:.3f} kilometers.'.format(math.sqrt((a-p)**2 + (b-q)**2))
	p, q = a, b
