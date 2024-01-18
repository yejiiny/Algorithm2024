mn = list(map(int, input().split(' ')))

for i in range(mn[0], mn[1]+1):
    p = 1
    if i == 1:
        continue
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            p = 0
            break
    if p:
        print(i)