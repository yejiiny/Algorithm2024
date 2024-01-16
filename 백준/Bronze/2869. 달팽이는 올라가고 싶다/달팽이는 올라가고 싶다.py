n = input().split(" ")

A = int(n[0])
B = int(n[1])
V = int(n[2])

now_meter = 0
day = 0

day = (V - A) // (A - B)

if (V - A) % (A - B) != 0:
    day += 2
else:
    day += 1


print(day)