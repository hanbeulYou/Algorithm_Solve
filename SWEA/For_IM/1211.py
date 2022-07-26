#import sys
import copy
#sys.stdin = open("SWEA/For_IM/input.txt", encoding='utf-8')

def move(floor, idx, ladders, cnt) :
    if floor == 100 :
        global dist
        dist = cnt
        return
    else :
        if 0 < idx < 99 :
            if ladders[floor][idx + 1] == 1 :
                ladders[floor][idx] = 2
                move(floor, idx + 1, ladders, cnt + 1)
            elif ladders[floor][idx - 1] == 1:
                ladders[floor][idx] = 2
                move(floor, idx - 1, ladders, cnt + 1)
            else :
                ladders[floor][idx] = 2
                move(floor + 1, idx, ladders, cnt + 1)

        elif idx == 0 :
            if ladders[floor][idx + 1] == 1 :
                ladders[floor][idx] = 2
                move(floor, idx + 1, ladders, cnt + 1)
            else :
                ladders[floor][idx] = 2
                move(floor + 1, idx, ladders, cnt + 1)
            
        else :
            if ladders[floor][idx - 1] == 1:
                ladders[floor][idx] = 2
                move(floor, idx - 1, ladders, cnt + 1)
            else :
                ladders[floor][idx] = 2
                move(floor + 1, idx, ladders, cnt + 1)

for _ in range(10) :
    test_case = int(input())
#    test_case = int(sys.stdin.readline())
    ladders = [0 for _ in range(100)]
    idx = 0
    for i in range(100) :
        ladders[i] = list(map(int, input().split()))
#        ladders[i] = list(map(int, sys.stdin.readline().split()))

    min_dist = 10000
    min_idx = 0
    for idx in range(100) :
        dist = 0
        if ladders[0][idx] == 1 :
            check = 0
            if test_case == 1 and (idx == 18 or idx == 37) :
                check = 1
                print(idx)
            copy_ladders = copy.deepcopy(ladders)
            move(0, idx, copy_ladders, 0)
            if min_dist > dist :
                min_dist = dist
                min_idx = idx
    
    print('#{}'.format(test_case), min_idx)