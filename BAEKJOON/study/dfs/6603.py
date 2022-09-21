from itertools import combinations
while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    nums = arr[1:arr[0]+1]
    answers = list(combinations(nums, 6))
    for answer in answers:
        print(*answer)
    print()