import math

def is_prime(num):
    cnt = 0
    for i in range(2, int(math.sqrt(num))+1):
        if not num%i:
            cnt += 1
    if cnt == 0 and num != 1:
        return True
    return False

def solution(n, k):
    my_n = ''
    while n >= k:
        my_n += chr(ord('0')+n%k)
        n//=k
    my_n += chr(ord('0')+n%k)
    my_n = my_n[::-1]

    my_arr = list(my_n.split('0'))
    answer = 0
    for my_num in my_arr:
        if my_num == '':
            continue
        if is_prime(int(my_num)):
            answer += 1
    return answer


# print(solution(437674, 3))
print(solution(110011, 10))