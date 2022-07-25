#import sys

for _ in range(1, 11) :
#    test_case = int(sys.stdin.readline())
    test_case = int(input())
    table = [0 for _ in range(100)]
    max_sum = 0
    for i in range(100) :
#        table[i] = list(map(int, sys.stdin.readline().split()))
        table[i] = list(map(int, input().split()))
        if max_sum < sum(table[i]) :
            max_sum = sum(table[i])
    
    for i in range(100) :
        sum_col = 0
        for j in range(100) :
            sum_col += table[j][i]
        if max_sum < sum_col :
            max_sum = sum_col
    
    
    sum_diag_up = 0
    sum_diag_down = 0
    for i in range(100) :
        sum_diag_up += table[i][99 - i]
        sum_diag_down += table[i][i]
        
    if max_sum < sum_diag_up :
        max_sum = sum_diag_up
    if max_sum < sum_diag_down :
        max_sum = sum_diag_down
        
    print('#{}'.format(test_case), max_sum)