a = input().split(' ')
c = int(input())
n0 = int(input())


a1 = int(a[0])
a0 = int(a[1])

result = 1


for i in range (n0, 100):
    fn = a1 * i + a0
    gn = i


    if c * gn < fn:
        result = 0
        break


print(result)