n = int(raw_input())
i = 1
ans = 0
while n/i - i + 1 >= 0:
	ans += n/i - i + 1
	i += 1
print ans
