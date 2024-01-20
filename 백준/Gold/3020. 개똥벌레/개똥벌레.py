import sys
input = sys.stdin.readline
from bisect import bisect_left

n, h = map(int, input().split(" "))
top = []
bottom = []

for i in range(n):
    walls = int(input())
    if i % 2 == 0:
        top.append(walls)
    else:
        bottom.append(walls)

top.sort()
bottom.sort()

cnt = 1
min = n
for i in range(1, h+1):
    t = bisect_left(top, h+1-i)
    b = bisect_left(bottom, i)

    if n-(t+b) < min:
        min = n-(t+b)
        cnt = 1
    elif n-(t+b) == min:
        cnt += 1

print(min, cnt)