T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    puzzle = [[0 for i in range(n)] for j in range(n)] 

    for i in range(n) :
        puzzle[i] = list(map(int, input().split()))

    count = 0
    count_row = 0
    count_col = 0

    for i in range(n) :
        check_row = []
        for j in range(n) :
            if j == 0 :
                check_row.append(puzzle[i][j])
            else :
                if puzzle[i][j] == 0 :
                    check_row.append(0)
                else :
                    check_row.append(check_row[j-1] + puzzle[i][j])
                    check_row[j-1] = 0
        for j in range(n) :
            if check_row[j] == k :
                count_row += 1

    for i in range(n) :
        check_col = []
        for j in range(n) :
            if j == 0 :
                check_col.append(puzzle[j][i])
            else :
                if puzzle[j][i] == 0 :
                    check_col.append(0)
                else :
                    check_col.append(check_col[j-1] + puzzle[j][i])
                    check_col[j-1] = 0
        for j in range(n) :
            if check_col[j] == k :
                count_col += 1

    count = count_row + count_col
    print(f'#{test_case}', count)