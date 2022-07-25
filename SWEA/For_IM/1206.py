#import sys
#sys.stdin = open("SWEA/For_IM/input.txt", encoding='utf-8')

for test_case in range(1, 11) :
    n = int(input())
#    buildings = list(map(int, sys.stdin.readline().split()))
    buildings = list(map(int, input().split()))
    views = 0
    
    for idx, building in enumerate(buildings) :
        if idx < 2 or idx >= n - 2 :
            continue
        else :
            max_height = 0
            max_idx = 0
            for i in range(1, 3) :
                if max_height < buildings[idx - i] :
                    max_height = buildings[idx - i]
                    max_idx = idx - i
                if max_height < buildings[idx + i] :
                    max_height = buildings[idx + i]
                    max_idx = idx + i
            if max_height < building :
                views += building - max_height
        
    print('#{}'.format(test_case), views)