def check():
    for i in range(4):
        if tokens[i] == 32:
            continue
        for j in range(i+1, 4):
            if tokens[j] == 32:
                continue
            elif tokens[i] == tokens[j]:
                return False
    return True

def dfs(turn, token):
    global result
    global score

    if turn == 10:
        result = max(result, score)
        return
    
    # 움직일 칸 수
    move = arr[turn]
    # 시작 주소 저장
    tmp = tokens[token]
    # 10점 칸 시작
    if tmp == 5:
        tokens[token] = 21
        move -= 1
    # 20점 칸 시작
    if tmp == 10:
        tokens[token] = 25
        move -= 1
    # 30점 칸 시작
    if tmp == 15:
        tokens[token] = 27
        move -= 1
        
    while move:
        # 10, 20, 30에서 출발한 애들이 25에 도달할 경우
        if tokens[token] == 26 or tokens[token] == 29:
            tokens[token] = 24
            move -= 1
        # 25 출발
        elif tokens[token] == 24:
            tokens[token] = 30
            move -= 1
        # 35에서 40 가는길 처리
        elif tokens[token] == 31:
            tokens[token] = 20
            move -= 1
        # 40 도달시 move가 1개 이상 남으면 break
        elif tokens[token] == 20:
            tokens[token] = 32
            break
        else:
            tokens[token] += 1
            move -= 1
    
    if not check:
        tokens[token] = tmp
        return

    score += table[tokens[token]]
    
    for i in range(4):
        if tokens[i] != 32:
            dfs(turn+1, i)
            score -= table[tokens[token]]
            tokens[token] = tmp
    

table = [0, 2, 4, 6, 8, 10, 
        12, 14, 16, 18, 20, 
        22, 24, 26, 28, 30, 
        32, 34, 36, 38, 40, 
        13, 16, 19, 25, 
        22, 24,
        28, 27, 26, 
        30, 35, 0]

tokens = [0 for _ in range(4)]
arr = list(map(int, input().split()))
result, score = 0, 0
dfs(0, 0)
print(result)