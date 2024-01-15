n = int(input())

for i in range(n):
    star = i + 1
    blank = n - star
    for j in range(blank):
        print(' ', end="")

    for k in range(star):
        print('*', end="")

    print()

