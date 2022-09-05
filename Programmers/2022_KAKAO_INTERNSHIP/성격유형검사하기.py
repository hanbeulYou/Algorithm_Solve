def solution(surveys, choices):
    sur_idx = ['RT', 'CF', 'JM', 'AN',]
    arr = [0 for _ in range(4)]
    for idx, survey in enumerate(surveys):
        if survey == 'TR' or survey == 'FC' or survey == 'MJ' or survey == 'NA':
            choices[idx] = 8 - choices[idx]
            survey = survey[::-1]
        arr[sur_idx.index(survey)] += choices[idx] - 4
    
    answer = ''
    for idx in range(4):
        if arr[idx] > 0:
            answer += sur_idx[idx][1]
        else:
            answer += sur_idx[idx][0]
    return answer

#print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
