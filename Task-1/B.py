s = input()

count = 0
long_rep = 0
track_chr = ''

for char in s:
    if char == track_chr:
        count+=1
    else:
        track_chr = char
        count = 1
    
    long_rep = max(long_rep,count)

print(long_rep)