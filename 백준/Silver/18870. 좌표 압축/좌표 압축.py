n = int(input())
nums = list(map(int, input().split(" ")))

set_nums = list(set(nums))
set_nums.sort()
dic_nums = {set_nums[i] : i for i in range(len(set_nums))}

for value in nums:
    print(dic_nums[value], end=" ")