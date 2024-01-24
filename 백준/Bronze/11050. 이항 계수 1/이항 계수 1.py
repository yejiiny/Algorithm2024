import sys
input = sys.stdin.readline

n, k = map(int, input().split(" "))

a = n - k
n_fac = 1

while n > k:
    n_fac = n_fac * n
    n -= 1

a_fac = 1
while a > 0:
    a_fac = a_fac * a
    a -= 1

print(int(n_fac/a_fac))