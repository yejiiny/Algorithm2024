T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    bug = []
    for i in range(N):
        line = list(map(int, input().split()))
        bug.append(line)

    sum_list = []
    x, y = 0, 0

    while y < N:
        sum = 0

        for i in range(M):
            if y + i >= N: break
            for j in range(M):
                if x + j >= N: break
                sum += bug[y+i][x+j]

        sum_list.append(sum)

        x = (x + 1) % N
        if x == 0:
            y += 1
    print("#", end="")
    print(t, end=" ")
    print(max(sum_list))
