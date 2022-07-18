#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    count = 0

    for i in range(n) :
        alpha, num = input().split()
        num = int(num)

        for j in range(num) :
            print(alpha, end='')
            count += 1
            if count % 10 == 0 :
                print()
    
    print()