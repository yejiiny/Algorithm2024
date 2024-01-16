nums = input().split(' ')


n = int(nums[0])
m = int(nums[1])

bucket = []

for i in range (n):
    bucket.append(i+1)

for i in range (m):
    nums = input().split(' ')
    
    change1 = int(nums[0])
    change2 = int(nums[1])

    tmp = bucket[change1-1]
    bucket[change1-1] = bucket[change2-1]
    bucket[change2-1] = tmp

print(*bucket)

