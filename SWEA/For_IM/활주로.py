import sys

def check_left(road, x, check) :
    for i in range(0, x) :
        if check == 1 :
            return False
    for i in range(1, x) :
        if road[i] != 0 :
            return False
    else :
        return True

def check_right(road, x, check) :   
    for i in range(0, x) :
        if check == 1 :
            return False 
    for i in range(x - 1) :
        if road[i] != 0 :
            return False
    else :
        return False

def check_line(n, x, line) :
    tmp = [0 for _ in range(n)]
    new_line = [0 for _ in range(n)]
    for i in range(1, n) :
        new_line[i] = line[i] - line[i - 1]
    
    flag = 1
    for i in range(0, n) :        
        road_x = []
        tmp_x = []

        if new_line[i] == 1 :
            if i < x :
                flag = 0 # 불가능
            else :
                for j in range(x + 1) :
                    road_x.append(new_line[i - x + j])
                    tmp_x.append(tmp[i - x + j])
                if check_left(road_x, x + 1, tmp_x) :
                    for j in range(x + 1) :
                        tmp[i - x + j] = 1
                    continue
                else :
                    flag = 0
        
        elif new_line == - 1 :
            if i >= n - x :
                flag = 0
            else :
                for j in range(x + 1) :
                    road_x.append(new_line[i + j])
                    tmp_x.append(tmp[i + j])
                if check_right(road_x, x + 1, tmp_x) :
                    for j in range(x + 1) :
                        tmp[i - x + j] = 1
                    continue
                else :
                    flag= 0

        else :
            continue
    
    return flag


sys.stdin = open('SWEA\For_IM\input.txt')
#T = int(input())
T = int(sys.stdin.readline())
for test_case in range(1, T + 1) :
    #N, X = map(int, input().split())
    N, X = map(int, sys.stdin.readline().split())
    land = []
    cnt = 0

    for i in range(N) :
        land.append([])
    #    land[i] = list(map(int, input().split()))
        land[i] = list(map(int, sys.stdin.readline().split()))

    for i in range(N) :
        cnt += check_line(N, X, land[i])

    for i in range(N) :
        line = []
        for j in range(N) : 
            line.append(land[j][i])
        cnt += check_line(N, X, line)
    
    print(f'#{test_case} {cnt}')