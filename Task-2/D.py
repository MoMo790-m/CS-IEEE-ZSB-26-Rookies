n = int(input())
v = list(map(int, input().split()))

prefix_orig = [0] * (n + 1)
for i in range(n):
    prefix_orig[i + 1] = prefix_orig[i] + v[i]

u = sorted(v)

prefix_sorted = [0] * (n + 1)
for i in range(n):
    prefix_sorted[i + 1] = prefix_sorted[i] + u[i]


m = int(input())
for _ in range(m):
    query_type, l, r = map(int, input().split())
    
    if query_type == 1:
        print(prefix_orig[r] - prefix_orig[l - 1])
    else:
        print(prefix_sorted[r] - prefix_sorted[l - 1])