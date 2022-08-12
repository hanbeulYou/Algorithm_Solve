# 5432_쇠막대기 자르기
# 2022-08-12

#import sys
#sys.stdin = open('input.txt','r')

T = int(input())
# T = int(sys.stdin.readline())

def my_len(my_str) :
    cnt = 0
    for _ in my_str :
        cnt += 1
    return cnt

for tc in range(1, T+1) :
    bars = input()
    n = my_len(bars)
    level = 0
    pieces = 0
    idx = 0
    
    while idx < n :
        if bars[idx] == '(' :
            if bars[idx+1] == ')' :
                pieces += level
                idx += 2
            else :
                level += 1
                idx += 1
        else :
            pieces += 1
            level -= 1
            idx += 1
    
    print('#{} {}'.format(tc,pieces))