t_sum = 10

for test_case in range(t_sum):
    N = int(input())
    buildings = list(map(int, input().split()))

    ans = 0
    for j in range(2, N-2):
        highest = max(buildings[j-2], buildings[j-1], buildings[j+1], buildings[j+2])

        if buildings[j] > highest:
            ans += buildings[j] - highest

    print("#", end="")
    print(test_case + 1, ans)




