T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
num = 1
for test_case in range(1, T + 1):
    str = input()
    flag = 1
    
#    print(str, len(str))
    
    for i in range(len(str)) :
        if str[i] != str[len(str) - 1 - i] :
            flag = 0
    print(f'#{num}', flag)
    num += 1