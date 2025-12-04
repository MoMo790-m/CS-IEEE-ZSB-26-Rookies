n, x = map(int, input().split())
nums = list(map(int, input().split()))


ind = [(nums[i], i + 1) for i in range(n)]
ind.sort()

left = 0
right = n - 1

while left < right:
    current_sum = ind[left][0] + ind[right][0]
    
    if current_sum == x:
        print(ind[right][1], ind[left][1])
        exit()
    elif current_sum < x:
        left += 1
    else:
        right -= 1

print("IMPOSSIBLE")