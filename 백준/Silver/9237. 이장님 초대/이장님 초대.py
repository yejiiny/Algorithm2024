import sys
input = sys.stdin.readline

n = int(input())
days = list(map(int,input().split(' ')))

days.sort()
days.reverse()

plant = 1
max_grow = 0
grow = 0

for i in range(n):
    if max_grow <= days[i] + plant:
        max_grow = days[i] + plant

    plant += 1

print(max_grow+1)
