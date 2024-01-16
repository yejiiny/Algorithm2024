n = int(input())
grade = list(map(int, input().split(' ')))

m = max(grade)
sum = 0

for i in range (n):
    sum += grade[i]

average = sum/m * 100/n
print(average)