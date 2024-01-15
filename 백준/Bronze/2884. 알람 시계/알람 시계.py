n = input()
nums = n.split(' ')
h = int(nums[0])
m = int(nums[1])

if m < 45:
    h = h - 1
    m = m + 60

m = m - 45

if h < 0:
    h = h + 24

print(h,m)