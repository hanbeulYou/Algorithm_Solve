def can_cnt(arr1, arr2, n):
    idx = 0
    while idx < n :
        if arr1[idx] < arr2[idx]:
            return False
        idx += 1
    return True


def solution(want, number, discount):
    n = len(want)
    left = 0
    right = 9
    cnt = 0
    want_cnt = [0 for _ in range(n)]

    for i in range(10):
        if discount[i] in want:
            want_cnt[want.index(discount[i])] += 1

    if can_cnt(want_cnt, number, n) :
        cnt += 1

    while right < len(discount)-1:
        old = discount[left]
        if old in want:
            want_cnt[want.index(old)] -= 1
        left += 1

        right += 1
        new = discount[right]
        if new in want:
            want_cnt[want.index(new)] += 1

        if can_cnt(want_cnt, number, n) :
            cnt += 1
        
    return cnt


print(solution(['b','a','r','pork','pot'],[3,2,2,2,1], ['c', 'a', 'a', 'b', 'r', 'a', 'pork', 'b', 'pork', 'r', 'pot', 'b', 'a', 'b']))