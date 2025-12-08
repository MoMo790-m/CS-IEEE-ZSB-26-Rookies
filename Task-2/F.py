n, k, q = map(int, input().split())

max_temp = 200001


diff = [0] * (max_temp + 1)

for _ in range(n):
    l, r = map(int, input().split())
    diff[l] += 1
    diff[r + 1] -= 1


track = [0] * (max_temp + 1)
curr = 0
for i in range(max_temp + 1):
    curr += diff[i]
    track[i] = curr


admis = [0] * (max_temp + 1)
for i in range(max_temp + 1):
    if track[i] >= k:
        admis[i] = 1

prefix = [0] * (max_temp + 1)
for i in range(1, max_temp + 1):
    prefix[i] = prefix[i - 1] + admis[i]

for _ in range(q):
    a, b = map(int, input().split())
    res = prefix[b] - prefix[a - 1]
    print(res)