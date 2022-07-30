def solution(rows, columns, queries):
    min_list = []
    matrix = [[(i * columns + j + 1) for j in range(columns)] for i in range(rows)]

    for query in queries :
        x1, y1, x2, y2 = query[0] - 1, query[1] - 1, query[2] - 1, query[3] - 1
        x1_list, y1_list, x2_list, y2_list = [], [], [], []

        for idx in range(x2 - x1) :
            x1_list.append(matrix[x1 + 1 + idx][y1])
            x2_list.append(matrix[x1 + idx][y2])

        for idx in range(y2 - y1) :
            y1_list.append(matrix[x1][y1 + idx])
            y2_list.append(matrix[x2][y1 + 1 + idx])

        for idx in range(x2 - x1) :
            matrix[x1 + idx][y1] = x1_list[idx]
            matrix[x1 + 1 + idx][y2] = x2_list[idx]

        for idx in range(y2 - y1) :
            matrix[x1][y1 + idx + 1] = y1_list[idx]
            matrix[x2][y1 + idx] = y2_list[idx]

        min_list.append(min(x1_list + x2_list + y1_list + y2_list))

    return min_list