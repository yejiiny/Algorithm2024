charlist = list(input())

time = 0

for i in range (len(charlist)):
    num = int(ord(charlist[i])-ord('A'))//3+2
    time = time + num + 1
    
    if charlist[i] == 'S' or charlist[i] == 'V' or charlist[i] == 'Y' or charlist[i] == 'Z':
        time -=1
    

print(time)
