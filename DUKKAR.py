def factorial(x):
    result = 1
    for i in xrange(1,x+1):
        result *= i
    return result

def combination(n,r):
    return factorial(n)/(factorial(n-r)*factorial(r))

p = int(raw_input())
c = 0
for i in range(0,n+1):
    if combination(n,i) % p == 0:
        c += 1
print c
