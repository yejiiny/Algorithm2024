import sys
input = sys.stdin.readline

n, k = map(int, input().split(" "))
table = list(input())
table.remove(table[-1])

yam = 0
start = 0
end = 0
for i in range(n):
    if table[i] == 'P':
        start = i - k
        end = i + k + 1

        if i - k < 0:
            start = 0

        if i + k > n - 1:
            end = n

        for j in range(start, end):
            if table[j] == 'H':
                yam += 1
                table[j] = 'X'
                break

print(yam)

