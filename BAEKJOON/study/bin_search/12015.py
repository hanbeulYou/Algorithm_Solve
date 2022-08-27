N = int(input())
arr = list(map(int, input().split()))
new_arr = [0]
for item in arr:
    # 더 큰 값이 있으면 추가
    if new_arr[-1] < item:
        new_arr.append(item)
    else:
        s, e = 0, len(new_arr)
        # 이분탐색으로 시간 줄이기
        while s < e:
            m = (s+e)//2
            if new_arr[m] < item:
                s = m + 1
            else:
                e = m
        new_arr[e] = item
#    print(new_arr)

print(len(new_arr)-1)