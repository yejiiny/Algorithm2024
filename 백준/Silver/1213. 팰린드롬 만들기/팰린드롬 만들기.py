import sys
input = sys.stdin.readline

str = input()
str_list = list(str)
str_list.remove(str_list[-1])

char_list = list(set(str_list))
char_list.sort()

char_dic = {}
odd = 0
even = 0
odd_char = ''

for value in char_list:
    counts = str_list.count(value)
    if counts % 2 == 0:
        even += 1
    else:
        odd += 1
        odd_char = value
    char_dic[value] = counts

if odd > 1:
    print("I'm Sorry Hansoo")
else:
    result = []
    for i in range(len(char_list)):
        if char_list[i] != odd_char:
            for j in range(char_dic.get(char_list[i])//2):
                result.append(char_list[i])
        else:
            for j in range(char_dic.get(char_list[i])//2):
                result.append(char_list[i])

    print(''.join(result)+odd_char, end='')
    result.reverse()
    print(''.join(result))
