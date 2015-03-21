#import math
#while True:
#	n = int(raw_input())
#	if n == 0:
#		break
#	print '%.2f' %float((n*n / 2 / math.pi))
from math import pi

c = 1 / (2*pi)
while True:
   L = int(raw_input())
    if L == 0: break
    print '%.2f' % round(L*L*c, 2)
