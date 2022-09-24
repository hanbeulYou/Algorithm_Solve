def solution(n, m, x, y, r, c, k):
    move_to_x = abs(r-x)
    move_to_y = abs(c-y)
    answer_list = []
    if k < move_to_x + move_to_y:
        answer = 'impossible'
    for _ in range(move_to_x):
        if x > r:
            answer_list.append('d')
        else:
            answer_list.append('u')
    for _ in range(move_to_y):
        if y > c:
            answer_list.append('l')
        else:
            answer_list.append('r')
    return answer