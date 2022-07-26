#import sys

#sys.stdin = open("SWEA/For_IM/input.txt", encoding='utf-8')

for _ in range(10) :
    test_case = int(input())
    ladders = [0 for _ in range(100)]
    idx = 0
    for i in range(100) :
        ladders[i] = list(map(int, input().split()))
        if i == 99 :
            idx = ladders[i].index(2)
            
    floor = 99
    while floor > 0 :
        if 0 < idx < 99 :
            if ladders[floor][idx + 1] == 1 :
                ladders[floor][idx] = 0
                idx += 1
                continue
            elif ladders[floor][idx - 1] == 1:
                ladders[floor][idx] = 0
                idx -= 1
                continue
            else :
                floor -= 1
        elif idx == 0 :
            if ladders[floor][idx + 1] == 1 :
                ladders[floor][idx] = 0
                idx += 1
                continue
            else :
                floor -= 1
            
        else :
            if ladders[floor][idx - 1] == 1:
                ladders[floor][idx] = 0
                idx -= 1
                continue
            else :
                floor -= 1
    
    print('#{}'.format(test_case), idx)