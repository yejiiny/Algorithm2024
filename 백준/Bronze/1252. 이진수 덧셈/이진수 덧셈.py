n = input().split(' ')
sum = 0

def two_to_ten(n):
    result = 0
    n_list = list(n)

    for i in range (len(n)):
        if n_list[i] == '1':
            result = result + (2 **(len(n)-i-1))

    return result

def ten_to_two(n):
    result = []

    while n > 0:
        result.append(n%2)
        n = n//2

    return result


sum = two_to_ten(n[0])+ two_to_ten(n[1])
sum2 = list(reversed(ten_to_two(sum)))

if sum == 0:
    print(0)

for i in range (len(sum2)):
    print(sum2[i], end="")