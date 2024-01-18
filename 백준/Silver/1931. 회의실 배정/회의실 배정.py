n = int(input())
time = []

for i in range(n):
    time.append(list(map(int, input().split(' '))))

time.sort(key=lambda x: (x[1], x[0])) # 두 번째 값이 같을 경우 첫 번째 값 기준으로 오름차순

last = 0
cnt = 0
timetable = []

for i in range(len(time)):
    if time[i][0] >= last:
        last = time[i][1]
        cnt += 1
        timetable.append(time[i])
        continue
    else:
        continue

print(cnt)