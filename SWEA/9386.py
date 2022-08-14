import sys
sys.stdin = open('input.txt','r')

T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    arr = list(map(int, input()))
    one = False
    max_cnt = 0
    cnt = 0
    while arr :
        num = arr.pop()

        if one and num :
            cnt += num
        elif num :
            one = True
            cnt += num
        else :
            cnt = 0
            one = False
        if max_cnt < cnt :
            max_cnt = cnt
    print ('#{} {}'.format(test_case, max_cnt))