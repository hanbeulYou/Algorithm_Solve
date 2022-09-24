def check_point(ryan):
    global info

    apeach_score = 0
    ryan_score = 0
    for i in range(11):
        if info[i] < ryan[i]:
            ryan_score += i
        else:
            apeach_score += i
    if ryan_score > apeach_score:
        return True
    return False
    

def make_shoot(depth, n, shoot, flag, info):
    global answer

    if depth == n:
        if check_point(shoot):
            answer = shoot[:]
            flag = True
        return

    for i in range(11):
        shoot[i] += 1
        make_shoot(depth+1, n, shoot, flag, info)
        shoot[i] -= 1
        if flag:
            return


def solution(n, info):
    shoot = [0 for _ in range(11)]
    flag = False
    make_shoot(0, n, shoot, flag)

    return answer


print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))