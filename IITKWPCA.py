import collections
for _ in xrange(int(raw_input())):
	print len(collections.Counter(raw_input().split()))
