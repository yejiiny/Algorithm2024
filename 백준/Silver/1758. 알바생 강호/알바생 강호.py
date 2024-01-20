import sys
input = sys.stdin.readline

n = int(input())
tips = []

for i in range(n):
    tips.append(int(input()))
tips.sort(reverse=True)

result = 0
for i in range(n):
    if tips[i] - i > 0:
        result += (tips[i] - i)

print(result)
