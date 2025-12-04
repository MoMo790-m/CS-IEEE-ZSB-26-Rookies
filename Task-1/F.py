n = int(input())
nums = list(map(int, input().split()))

result = [0] * n  
stack = []

for i in range(n):
    while stack and nums[stack[-1]] >= nums[i]:
        stack.pop()
    
    result[i] = stack[-1] + 1 if stack else 0
    stack.append(i)

print(*result)