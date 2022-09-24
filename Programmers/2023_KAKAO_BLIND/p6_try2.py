def solution(n, m, x, y, r, c, k):
    move_to_x = abs(r-x)
    move_to_y = abs(c-y)
    answer_list = []
    if k < move_to_x+move_to_y or k%2 != (move_to_x+move_to_y)%2:
        answer = 'impossible'
    for _ in range(move_to_x):
        if x < r:
            answer_list.append('d')
        else:
            answer_list.append('u')
    for _ in range(move_to_y):
        if y > c:
            answer_list.append('l')
        else:
            answer_list.append('r')
    answer_list.sort()
    len_ans = len(answer_list)

    d_index = 0
    l_index = 0
    if 'd' in answer_list:
        d_index = len_ans-answer_list[::-1].index('d')-1
    if 'l' in answer_list:
        l_index = len_ans-answer_list[::-1].index('l')-1

    while len_ans < k:
        move_d_max = n-c
        for i in range(move_d_max, -1, -1):
            if len_ans+(i)*2 <= k:
                for j in range(i):
                    answer_list.insert(d_index+1, 'd')
                for j in range(i):
                    answer_list.insert(d_index+1, 'u')
                
    return answer

print(solution(3, 4, 2, 3, 3, 1, 5))
#print(solution(2, 2, 1, 1, 2, 2, 2))