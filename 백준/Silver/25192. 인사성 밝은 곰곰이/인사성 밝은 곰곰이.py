import sys
input = sys.stdin.readline

n = int(input())
member = []
cnt = 0

for i in range(n):
    chat = input().strip()

    if chat == "ENTER":
        cnt += len(list(set(member)))
        member.clear()
        continue

    member.append(chat)

cnt += len(list(set(member)))

print(cnt)