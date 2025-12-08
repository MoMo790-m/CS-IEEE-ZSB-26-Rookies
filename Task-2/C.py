with open('bcount.in', 'r') as fin:
    data = fin.read().split()

ix = 0
n = int(data[ix])
q = int(data[ix + 1])
ix += 2

cows = []
for i in range(n):
    cows.append(int(data[ix]))
    ix += 1

pref1 = [0] * (n + 1)
pref2 = [0] * (n + 1)
pref3 = [0] * (n + 1)

for i in range(1,n + 1):
    pref1[i] = pref1[i - 1] + (1 if cows[i - 1] == 1 else 0) 
    pref2[i] = pref2[i - 1] + (1 if cows[i - 1] == 2 else 0) 
    pref3[i] = pref3[i - 1] + (1 if cows[i - 1] == 3 else 0) 

results = []
for _ in range(q):
    a = int(data[ix])
    b = int(data[ix + 1])
    ix += 2
    
    track1 = pref1[b] - pref1[a - 1]
    track2 = pref2[b] - pref2[a - 1]
    track3 = pref3[b] - pref3[a - 1]
    
    results.append(f"{track1} {track2} {track3}")
    
with open('bcount.out', 'w') as fout:
    fout.write('\n'.join(results) + '\n')