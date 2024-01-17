str = input()
bomb = input()

stack = []
bomb_len = len(bomb)


for i in range(len(str)):
    stack.append(str[i])
    if ''.join(stack[-bomb_len:]) == bomb:
        for _ in range(bomb_len):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")