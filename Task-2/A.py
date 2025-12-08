n, q = map(int, input().split())
arr = list(map(int, input().split()))


prefix = [0] * (n +1)
prefix[0] = 0


for i in range(n):
    prefix[i + 1] = prefix[i] + arr[i]

res  = []
for _ in range(q):
    a, b = map(int, input().split())
    res.append(prefix[b] - prefix[a - 1])

for ans in res:
    print(ans)