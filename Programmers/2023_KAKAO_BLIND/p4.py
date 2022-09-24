def is_connected(node, r_depth, connect):
    global answer
    global bin_num
    if bin_num[node-1] == '0':
        connect = False

    if r_depth == 1:
        if not connect:
            if bin_num[node-2] or bin_num[node]:
                return False
        return True

    left_connect = is_connected(node-2**(r_depth-1), r_depth-1, connect)
    right_connect = is_connected(node+2**(r_depth-1), r_depth-1, connect)
    if left_connect and right_connect:
        return True
    return False

def solution(numbers):
    global answer
    global bin_num
    answer = []
    
    for number in numbers:
        bin_num = bin(number).lstrip('0b')
        tmp = 0
        n = len(bin_num)
        while True:
            tmp += 1
            if 2**tmp-1 < n <= 2**(tmp+1)-1:
                bin_num = '0'*(2**(tmp+1)-1-n) + bin_num
                break
        bin_num = list(bin_num)
        
        if bin_num[tmp]:
            if is_connected(2**tmp, tmp, True):
                answer.append(1)
            else:
                answer.append(0)
        else:
            answer.append(0)

    return answer

print(solution([63, 111, 95]))