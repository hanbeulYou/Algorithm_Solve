def sequence(nums) :
    if len(nums) == 1 :
        return True
    diff = int(nums[0]) - int(nums[1])

    for idx, num in enumerate(nums) :
        if idx == len(nums) - 1 :
            break
        if int(num) - int(nums[idx + 1]) != diff :
            return False
    
    return True

n = int(input())
cnt = 0
for num in range(1, n + 1) :
    if sequence(str(num)) :
        cnt += 1

print(cnt)