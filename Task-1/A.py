X = int(input())
N = int(input())
W = list(map(int, input().split()))

Q = int(input())

P = []
for _ in range(Q):
    P.append(int(input()))
    
curr_weight = X 

track = [False] * N

for j in P:
    i = j - 1
    if not track[i]:
        curr_weight+= W[i]
        track[i] = True
    else:
        curr_weight-= W[i]
        track[i] = False
    
    print(curr_weight)