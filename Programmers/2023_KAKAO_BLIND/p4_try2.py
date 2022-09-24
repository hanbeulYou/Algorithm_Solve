def solution(numbers):
    answer = []

    for number in numbers:
        bin_num = bin(number).lstrip('0b')
        tmp = 0
        n = len(bin_num)
        while True:
            if 2**tmp-1 < n <= 2**(tmp+1)-1:
                bin_num = '0'*(2**(tmp+1)-1-n) + bin_num
                n = 2**(tmp+1)-1
                break
            tmp += 1
        bin_num = list(bin_num)
        
        case_answer = 1
        for depth in range(tmp):
            if case_answer != 1: break
            odd = True
            for idx in range(1, (n+1)//(2**depth)):
                if case_answer != 1: break

                new_idx = idx * (2**depth)
                if idx%2 == 1:
                    if odd:
                        if bin_num[new_idx-1] == '1' and bin_num[new_idx-1+(2**depth)] == '0':
                            case_answer = 0
                        odd = False
                    else:
                        if bin_num[new_idx-1] == '1' and bin_num[new_idx-1-(2**depth)] == '0':
                            case_answer = 0
                        odd = True
        answer.append(case_answer)

    return answer

print(solution([63, 111, 95]))