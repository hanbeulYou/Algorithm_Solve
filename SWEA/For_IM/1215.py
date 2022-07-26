#import sys

#sys.stdin  = open("SWEA/For_IM/input.txt", encoding='utf-8')

def check(i, j, n) :
    global table
    flag = [1, 1]
    move = 0
    while move < n :
        if (j + move) < 8 and j + (n - 1 - move) < 8 : # 우측 확인
            if table[i][j + move] != table[i][j + (n - 1 - move)] : 
                flag[0] = 0
        else :
            flag[0] = 0
        if (i + move) < 8 and i + (n - 1 - move) < 8: # 하측 확인
            if table[i + move][j] != table[i + (n - 1 - move)][j] : 
                flag[1] = 0
        else :
            flag[1] = 0
        move += 1
    return (sum(flag))


for test_case in range(1, 11) :
#    n = int(sys.stdin.readline())
    n = int(input())
    table = [0 for _ in range(8)]
    cnt = 0

    for i in range(8) :
#        table[i] = list(sys.stdin.readline())
        table[i] = list(input())
    
    for i in range(8) :
        for j in range(8) :
            cnt += check(i, j, n)
    
    print('#{}'.format(test_case), cnt)