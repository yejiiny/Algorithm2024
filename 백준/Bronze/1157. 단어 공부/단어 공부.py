char = input()
char = char.upper()

cnt = []
checklist = []
charlist = list(char)

for i in range (len(charlist)):
    cnt.append(0)

    if charlist[i] in checklist:
        continue

    for j in range (len(charlist)):
        if charlist[i] == charlist[j]:
            cnt[i] += 1
    
    checklist.append(charlist[i])


if cnt.count(max(cnt)) !=1:
    print("?")

else:
    print(charlist[cnt.index(max(cnt))])
