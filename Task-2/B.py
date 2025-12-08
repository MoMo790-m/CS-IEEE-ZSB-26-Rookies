t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    
    prefix = [0] * (n + 1)
    
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]
        
    orig_sum = prefix[n]
        
        
    for _ in range(q):
        l, r, k = map(int, input().split())
        pre_sum = prefix[r] - prefix[l - 1]
        track = r - l + 1
        res = orig_sum - pre_sum + (track * k)
            
        if res % 2 == 1:
            print('Yes')
        else:
            print('No')

