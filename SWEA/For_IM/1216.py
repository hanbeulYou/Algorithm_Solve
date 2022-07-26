import sys

sys.stdin  = open("SWEA/For_IM/input.txt", encoding='utf-8')

def check(i, j, n) :
    global table
    flag = [1, 1]
    move = 0
    while move < n :
        if (j + move) < 100 and j + (n - 1 - move) < 8 : # 우측 확인
            if table[i][j + move] != table[i][j + (n - 1 - move)] : 
                flag[0] = 0
        else :
            flag[0] = 0
        if (i + move) < 100 and i + (n - 1 - move) < 8: # 하측 확인
            if table[i + move][j] != table[i + (n - 1 - move)][j] : 
                flag[1] = 0
        else :
            flag[1] = 0
        move += 1
    return (sum(flag))


for _ in range(1, 11) :
    test_case = int(sys.stdin.readline())
#    test_case = int(input())
    table = [0 for _ in range(100)]
    cnt = 0

    for i in range(100) :
        table[i] = list(sys.stdin.readline())
#        table[i] = list(input())
    
    max_len = 0
    for i in range(100) :
        for j in range(100) :
            for n in range(min((100 - i), (100 - j)), -1, -1) :
                c = check(i, j, n)
                if c != 0:
                    if max_len < n :
                        max_len = n
                else :
                    break
    
    print('#{}'.format(test_case), cnt)