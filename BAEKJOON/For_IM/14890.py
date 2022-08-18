#14890_경사로 풀이
#2022-08-18

def check(arr) :
    global N, L
    check = [0] * N
    idx = 0
    step = 0

    while idx < N - 1 :
        step = arr[idx+1] - arr[idx]
        # 다음 칸과 한칸 이상 차이날 때
        if step > 1 or step < -1 :
            return 0

        # 다음 칸이 한칸 더 높을 때
        elif step == 1 :
            # 왼쪽 확인
            if idx >= L-1 :
                for i in range(idx-L+1, idx+1) :
                    # 경사로를 놓는 범위가 평평하지 않을 경우
                    if arr[i] != arr[idx] : return 0
                    else : check[i] += 1
                idx += 1
            else :
                return 0

        # 다음 칸이 한칸 더 낮을 때
        elif step == -1 :
            # 오른쪽 확인
            if idx <= N-L-1 :
                for i in range(idx+1, idx+L+1) :
                    # 경사로를 놓는 범위가 평평하지 않을 경우
                    if arr[i] != arr[idx+1] : return 0
                    else : check[i] += 1
                idx += 1
            else :
                return 0
        
        else :
            idx += 1
    # check는 한번 경사로를 놓은 곳은 다른 경사로 못 놓게
    for i in range(N) :
        if check[i] > 1 : return 0
    return 1


N, L = map(int, input().split())
table = []

for i in range(N) :
    table.append(list(map(int, input().split())))

cnt = 0
for i in range(N) :
    col = []
    for j in range(N) :
        col.append(table[j][i])
    # 세로열 확인
    cnt += check(col)
    # 가로행 확인
    cnt += check(table[i])

print(cnt)