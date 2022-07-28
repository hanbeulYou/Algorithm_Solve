import sys
sys.stdin = open('SWEA\For_IM\input.txt')

def drop_N(table, n) :
    idx = n - 1
    while table[idx] != 2 :
        if idx == 0 :
            break
        table[idx] = 0
        idx -= 1
        
def drop_S(table, n) :
    idx = 0
    while table[idx] != 1 :
        if idx == n - 1 :
            break
        table[idx] = 0
        idx += 1

def cnt_NS(table, n) :
    NS = 1
    cnt = 0
    for i in range(n) :
        if NS == 1 and table[i] == 2 :
            NS = 2
            cnt += 1
        if NS == 2 and table[i] == 1 :
            NS = 1
    return cnt

for test_case in range(1, 11) :
    n = int(input())
    table = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(100) :
        table[i] = list(map(int, input().split()))
    
    cnt = 0
    for i in range(100) :
        table_col = []
        for j in range(100) :
            table_col.append(table[j][i])
        drop_N(table_col, n)
        drop_S(table_col, n)
        cnt += cnt_NS(table_col, n)
    
    print(f'#{test_case} {cnt}')