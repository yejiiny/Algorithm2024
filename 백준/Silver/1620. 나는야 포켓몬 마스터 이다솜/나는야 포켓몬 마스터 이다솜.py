n = list(map(int, input().split(" ")))

dic = {}
test =[]

for i in range(n[0]):
    dic[input()] = i + 1

for i in range(n[1]):
    test.append(input())

dic_keys = list(dic.keys())

for value in test:
    if dic.get(value):
        print(dic.get(value))
    else:
        print(dic_keys[int(value)-1])