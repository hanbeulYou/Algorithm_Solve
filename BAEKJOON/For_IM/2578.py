def check() :
    sum_diag_1 = 0
    sum_diag_2 = 0
    cnt_bingo = 0

    for i in range(5) :
        sum_col = 0
        sum_row = 0
        for j in range(5) :
            sum_col += check_table[i][j]
            sum_row += check_table[j][i]
        if sum_col == 5 : 
            cnt_bingo += 1
        if sum_row == 5 :
            cnt_bingo += 1
        
        sum_diag_1 += check_table[i][i]
        sum_diag_2 += check_table[4-i][i]
    
    if sum_diag_1 == 5 :
        cnt_bingo += 1
    if sum_diag_2 == 5 :
        cnt_bingo += 1
    
    return cnt_bingo

def call_table(call) :
    global table
    global check_table
    for i in range(5) :
        for j in range(5) :
            if table[i][j] == call :
                check_table[i][j] = 1
                if check() >= 3 :
                    return True
    return False

table = []
call = []
check_table = [[0 for _ in range(5)] for __ in range(5)]
for _ in range(5) :
    table.append(list(map(int, input().split())))

for _ in range(5) :
    call.append(list(map(int, input().split())))

terminate = False
for i in range(5) :
    for j in range(5) :
        if call_table(call[i][j]) :
            print(i * 5 + j + 1)
            terminate = True
            break
    if terminate :
        break