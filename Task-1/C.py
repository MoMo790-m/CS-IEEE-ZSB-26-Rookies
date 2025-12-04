num = int(input())

sum_nums = num * (num + 1) // 2
group1 = []
group2 = []

if sum_nums % 2 == 0:
    print('YES')
    mid_num = sum_nums // 2
    for n in range(num,0,-1):
        if n <=  mid_num:
            group1.append(n)
            mid_num-=n
        else:
            group2.append(n)
    
    print(len(group1))
    print(*group1)
    
    print(len(group2))
    print(*group2)
else:
    print('NO')