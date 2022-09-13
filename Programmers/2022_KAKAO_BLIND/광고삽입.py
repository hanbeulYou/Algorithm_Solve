def solution(play_time, adv_time, logs):
    p_h, p_m, p_s = map(int, play_time[0:8].split(':'))
    a_h, a_m, a_s = map(int, adv_time[0:8].split(':'))
    play = p_h * 3600 + p_m * 60 + p_s
    adv = a_h * 3600 + a_m * 60 + a_s

    times = [0 for _ in range(play+1)]
    for log in logs:
        s_h, s_m, s_s = map(int, log[0:8].split(':'))
        e_h, e_m, e_s = map(int, log[9:17].split(':'))
        s = s_h * 3600 + s_m * 60 + s_s
        e = e_h * 3600 + e_m * 60 + e_s
        for i in range(s, e+1):
            times[i] += 1

    sum_v = 0
    for i in range(adv):
        sum_v += times[i]
    max_v = sum_v    
    max_idx = 0
    for i in range(1, play-adv+1):
        sum_v = sum_v - times[i-1] + times[i+adv]
        if max_v < sum_v:
            max_v = sum_v
            max_idx = i

    answer = ''
    if max_idx//3600 < 10:
        answer += '0' + str(max_idx//3600)
    else :
        answer += str(max_idx//3600)
    answer += ':'
    max_idx %= 3600
    if max_idx//60 < 10:
        answer += '0' + str(max_idx//60)
    else :
        answer += str(max_idx//60)
    max_idx %= 60
    answer += ':'
    if max_idx < 10:
        answer += '0' + str(max_idx)
    else :
        answer += str(max_idx)
    return answer

print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
# print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))