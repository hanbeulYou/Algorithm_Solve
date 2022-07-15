#import sys
#sys.stdin = open("input.txt", "r")
#T = int(sys.stdin().readline())

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    str_a = input().split()
    str_b = input().split()

    max = 0

    if n >= m :
        for i in range(n - m + 1) :
            sum = 0
            for j in range(m) :
                sum += int(str_a[i + j]) * int(str_b[j])
            if max < sum :
                max = sum
    
    else :
        for i in range(m - n + 1) :
            sum = 0
            for j in range(n) :
                sum += int(str_b[i + j]) * int(str_a[j])
            if max < sum :
                max = sum

    print (f'#{test_case}', max)