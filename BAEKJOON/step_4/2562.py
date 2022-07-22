nums = []
max_num = 0
max_idx = 0
for idx in range(9) : 
    nums.append(int(input()))
    if max_num < nums[idx] :
        max_num = nums[idx]
        max_idx = idx
print(max_num)
print(max_idx + 1)