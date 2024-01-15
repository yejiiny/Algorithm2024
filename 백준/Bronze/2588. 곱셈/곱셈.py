n1 = int(input())
n2 = int(input())
num = [n1,n2]

n3 = num[0] * (num[1]%10)
n4 = num[0] * ((num[1]%100)//10)
n5 = num[0] * (num[1]//100)
n6 = n3 + n4*10 + n5*100

print(n3)
print(n4)
print(n5)
print(n6)