n = int(input())
tops = list(map(int, input().split(' ')))

stack = []

for i in range(len(tops)):
    if not stack:
        print(0, end=" ")
    else:
        while stack[-1][1] < tops[i]:
            stack.pop()
            if not stack:
                print(0, end=" ")
                break
        if stack:
            print(stack[-1][0]+1, end=" ")

    stack.append([i, tops[i]])