T = int(input())

for test_case in range(1, T+1) :
    n, m = map(int, input().split())

    table = [[0 for i in range(n)] for j in range(n)]
    for i in range(n) :
        table[i] = list(map(int, input().split()))

    max = 0
    for i in range(n-m+1) :
        for j in range(n-m+1) :
            count = 0
            for k in range(m) :
                for l in range(m) :
                    count += table[i+k][j+l]
            if max < count :
                max = count
    
    print(f'#{test_case}', max)
