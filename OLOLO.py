# import collections
# s = ""
# for _ in xrange(int(raw_input())):
# 	a = raw_input()
# 	s += a
# 	c = collections.defaultdict(int)
# 	for i in s:
# 		c[i] += 1
# print min(c, key=c.get)

# Got TLE for the above algorithm

ans = 0
for _ in xrange(int(raw_input())):
	ans ^= int(raw_input())

print ans
