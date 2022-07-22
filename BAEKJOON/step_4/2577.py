A = int(input())
B = int(input())
C = int(input())
num = A * B * C
check_num = [0 for _ in range(10)]
while num > 0 :
    check_num[num % 10] += 1
    num //= 10
for check in check_num :
    print(check)