def solution(X, Y):
    X = list(X)
    Y = list(Y)
    X.sort(reverse=True)
    Y.sort(reverse=True)
    x,y = 0, 0
    n_x, n_y = len(X), len(Y)
    answer = ''
    len_ans = 0
    while x < n_x and y < n_y :
        if X[x] == Y[y]:
            answer += X[x]
            len_ans += 1
            x += 1
            y += 1
        elif X[x] > Y[y]:
            x += 1
        else:
            y += 1
    if len_ans > 1 and answer[0] == '0':
        return '0'
    elif answer != '':
        return answer
    else:
        return '-1'

print(solution('100', '2345'))