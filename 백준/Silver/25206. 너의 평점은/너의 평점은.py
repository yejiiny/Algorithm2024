gradelist = []

for i in range(20):
    list = input().split(' ')
    gradelist.append(list)

def grade_convert(grade):
    if grade == 'A+':
        return 4.5
    elif grade == 'A0':
        return 4.0
    elif grade == 'B+':
        return 3.5
    elif grade == 'B0':
        return 3.0
    elif grade == 'C+':
        return 2.5
    elif grade == 'C0':
        return 2.0
    elif grade == 'D+':
        return 1.5
    elif grade == 'D0':
        return 1.0
    elif grade == 'F':
        return 0.0
    return 0


gpa = 0
credit_sum = 0

for i in range(len(gradelist)):

    if gradelist[i][2] == 'P':
        continue

    credit = float(gradelist[i][1])
    grade = grade_convert(gradelist[i][2])

    gpa = gpa + credit * grade
    credit_sum += credit



print(gpa/credit_sum)

