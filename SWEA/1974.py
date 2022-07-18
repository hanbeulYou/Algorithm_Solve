def check_row(table) :
    for i in range(9) :
        check = [0 for j in range(10)]
        return_value = 1
        for j in range(9) :
            if check[table[i][j]] == 0 :
                check[table[i][j]] += 1
            else :
                return_value = 0
                break
        if return_value == 0 :
            break
    return return_value

def check_col(table) :
    for i in range(9) :
        check = [0 for j in range(10)]
        return_value = 1
        for j in range(9) :
            if check[table[j][i]] == 0 :
                check[table[j][i]] += 1
            else :
                return_value = 0
                break
        if return_value == 0 :
            break

    return return_value

def check_sqr(table) :
    for i in [0, 3, 6] :
        for j in [0, 3, 6] :
            check = [0 for k in range(10)]
            return_value = 1
            for k in range(3) :
                for l in range(3) :
                    if check[table[i+k][j+l]] == 0 :
                       check[table[i+k][j+l]] += 1
                    else :
                        return_value = 0
            if return_value == 0 :
                break
        if return_value == 0 :
            break
    
    return return_value

T = int(input())

for test_case in range(1, T + 1) :
    table = [[0 for i in range(9)] for j in range(9)]
    
    for i in range(9) :
        table[i] = list(map(int, input().split()))
    
    print(f'#{test_case}', end=' ')
    if check_col(table) == 1 and check_row(table) == 1 and check_sqr(table) == 1 :
        print(1)
    else : print(0)