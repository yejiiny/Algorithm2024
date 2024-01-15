n = input()
n2 = input()

now = n.split(' ')
time = int(n2)

m = int(now[1]) + time
h = int(now[0])

if m >= 60:
    h += m//60
    m = m%60

if h >= 24:
    h -= 24

print(h,m)