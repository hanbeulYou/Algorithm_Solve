def solution(arr1, arr2):
    answer = []
    for n in range(len(arr1)) :
        answer.append([])
        for m in range(len(arr2[0])) :
            value = 0
            for k in range(len(arr1[n])) :
                value += arr1[n][k] * arr2[k][m]
            answer[n].append(value)
    return answer

"""
arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4], [2, 4], [3, 1]]
print(solution(arr1, arr2))
"""