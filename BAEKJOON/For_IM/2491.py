n = int(input())
nums = [0 for i in range(n)]
nums = list(map(int,input().split()))

up, down, max_count = 1, 1, 1
for idx, num in enumerate(nums) :
    if idx == 0 : continue

    if nums[idx - 1] <= nums[idx] :
        up += 1
    else :
        up = 1
    if max_count < up :
        max_count = up

    if nums[idx - 1] >= nums[idx] :
        down += 1
    else :
        down = 1
    if max_count < down :
        max_count = down

print (max_count)