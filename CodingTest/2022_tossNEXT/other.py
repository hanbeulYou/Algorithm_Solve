# greedy를 활용해 무거운 애들 순으로 넣어서 트럭 보내기

def solution(M, load):
    load.sort(reverse=True)
    answer = 0
    while load :
        sum_load = 0
        idx = 0
        n = len(load)
        while idx < n :
            if sum_load + load[idx] <= M :
                sum_load += load.pop(idx)
                n -= 1
            else :
                idx += 1 
        answer += 1
    return answer

print(solution(13, [7,13,11,6,5,7,1,9,11,5]))