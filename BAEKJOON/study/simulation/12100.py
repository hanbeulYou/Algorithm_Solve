def make_board(dir, tmp_board):
    # 오른쪽으로 밀 때
    if dir == 'r':
        for i in range(N):
            new_arr = []
            # 해당 행에 숫자가 존재할 때 new_arr에 넣어줌
            for j in range(N):
                if tmp_board[i][j]:
                    new_arr.append(tmp_board[i][j])
                    tmp_board[i][j] = 0
            # 오른쪽 끝에부터 같은 값이 붙어있을 때 2배 후 옆에 친구는 0으로 바꿔줌
            for j in range(len(new_arr)-1, 0, -1):
                if new_arr[j] == new_arr[j-1]:
                    new_arr[j] *= 2
                    new_arr[j-1] = 0
            # new_arr에 숫자가 0이 아닐때 기존 board의 행에 오른쪽부터 차곡차곡 넣어줌
            idx = N-1
            for j in range(len(new_arr)-1, -1, -1):
                if new_arr[j]:
                    tmp_board[i][idx] = new_arr[j]
                    idx -= 1
    # 왼쪽으로 밀 때
    if dir == 'l':
        for i in range(N):
            new_arr = []
            for j in range(N):
                if tmp_board[i][j]:
                    new_arr.append(tmp_board[i][j])
                    tmp_board[i][j] = 0
            for j in range(len(new_arr)-1):
                if new_arr[j] == new_arr[j+1]:
                    new_arr[j] *= 2
                    new_arr[j+1] = 0
            idx = 0
            for j in range(len(new_arr)):
                if new_arr[j]:
                    tmp_board[i][idx] = new_arr[j]
                    idx += 1
    # 위쪽으로 밀 때
    if dir == 'u':
        for j in range(N):
            new_arr = []
            for i in range(N):
                if tmp_board[i][j]:
                    new_arr.append(tmp_board[i][j])
                    tmp_board[i][j] = 0
            for i in range(len(new_arr)-1):
                if new_arr[i] == new_arr[i+1]:
                    new_arr[i] *= 2
                    new_arr[i+1] = 0
            idx = 0
            for i in range(len(new_arr)):
                if new_arr[i]:
                    tmp_board[idx][j] = new_arr[i]
                    idx += 1
    # 아래쪽으로 밀 때
    if dir == 'd':
        for j in range(N):
            new_arr = []
            for i in range(N):
                if tmp_board[i][j]:
                    new_arr.append(tmp_board[i][j])
                    tmp_board[i][j] = 0
            for i in range(len(new_arr)-1, 0, -1):
                if new_arr[i] == new_arr[i-1]:
                    new_arr[i] *= 2
                    new_arr[i-1] = 0
            idx = N-1
            for i in range(len(new_arr)-1, -1, -1):
                if new_arr[i]:
                    tmp_board[idx][j] = new_arr[i]
                    idx -= 1
    return tmp_board


def dfs(dir, cnt, new_board):
    global result
    if cnt == 5:
        result = max(result, max(map(max, new_board)))
        return

    tmp_board = [0 for _ in range(N)]
    for i in range(N):
        tmp_board[i] = new_board[i][:]

    make_board(dir, tmp_board)
    # 4방향 탐색
    for d in dirs:
        dfs(d, cnt+1, tmp_board)

N = int(input())
board = list()
result = 0
for _ in range(N):
    board.append(list(map(int, input().split())))
    
dirs = ['r', 'l', 'u', 'd']
for d in dirs:
    dfs(d, 0, board)
print(result)