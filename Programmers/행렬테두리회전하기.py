def solution(rows, columns, queries):
    min_list = []
    matrix = [[(i * columns + j + 1) for j in range(columns)] for i in range(rows)] # 매트릭스 선언

    for query in queries :
        x1, y1, x2, y2 = query[0] - 1, query[1] - 1, query[2] - 1, query[3] - 1 # 입력 받은 값 할당
        x1_list, y1_list, x2_list, y2_list = [], [], [], []

        for idx in range(x2 - x1) : # 왼쪽 변에서 위로 움직일 부분 및 오른쪽 변에서 아래로 움직일 부분 -> 임시 list에 저장
            x1_list.append(matrix[x1 + 1 + idx][y1])
            x2_list.append(matrix[x1 + idx][y2])

        for idx in range(y2 - y1) : # 위쪽 변에서 오른쪽으로 움직일 부분 및 아래 변에서 왼쪽으로 움직일 부분 -> 임시 list에 저장
            y1_list.append(matrix[x1][y1 + idx])
            y2_list.append(matrix[x2][y1 + 1 + idx])

        for idx in range(x2 - x1) : # 저장한 list를 각자 움직일 방향에다 넣어주기
            matrix[x1 + idx][y1] = x1_list[idx]
            matrix[x1 + 1 + idx][y2] = x2_list[idx]

        for idx in range(y2 - y1) :
            matrix[x1][y1 + idx + 1] = y1_list[idx]
            matrix[x2][y1 + idx] = y2_list[idx]

        min_list.append(min(x1_list + x2_list + y1_list + y2_list))

    return min_list