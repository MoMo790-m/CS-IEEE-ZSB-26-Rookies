import math 

n = int(input())
a = list(map(int, input().split()))

prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = math.gcd(prefix[i], a[i])

suffix = [0] * (n + 1)
for i in range(n - 1,-1,-1):
    suffix[i] = math.gcd(suffix[i + 1], a[i])

res = 0

for i in range(n):
    curr_gcd = math.gcd(prefix[i], suffix[ i + 1])
    res = max(res,curr_gcd)

print(res) 