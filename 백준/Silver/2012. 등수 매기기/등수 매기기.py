import sys
input = sys.stdin.readline

n = int(input())
rank = []

for i in range(n):
    rank.append(int(input()))
rank.sort()
result = 0

for i in range(len(rank)):
    if rank[i] == i + 1:
        continue
    else:
        result += (abs((i + 1) - rank[i]))

print(result)