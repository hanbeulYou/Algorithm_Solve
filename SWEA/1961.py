T = int(input())

for test_case in range(1, T+1) :
    n = int(input())
    table = [[0 for i in range(n)] for j in range(n)]
    table_turn = [[[0 for i in range(n)] for j in range(n)] for k in range(3)]

    for i in range(n) :
        table[i] = list(map(int, input().split()))

    for i in range(n) :
        for j in range(n) :
            table_turn[0][j][n-i-1] = table[i][j]
            table_turn[1][n-i-1][n-j-1] = table[i][j]
            table_turn[2][n-j-1][i] = table[i][j]

    print(f'#{test_case}')
    for i in range(n) :
        for k in range(3) :
            for j in range(n) :
                print(table_turn[k][i][j], end='')
            print(' ', end='')
        print()