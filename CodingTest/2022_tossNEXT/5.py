def solution(tasks):
    cnt = 0
    tasks.sort()
    n = len(tasks)

    for idx, task in enumerate(tasks) :
        task_cnt = tasks.count(task)
        if task_cnt < 2 :
            return -1
        else :
            if task_cnt % 3 > 0:
                cnt += task_cnt // 3 + 1
            else :
                cnt += task_cnt // 3
        while idx < n - 1 :
            if tasks[idx] == tasks[idx + 1] :
                del tasks[idx + 1]
                n -= 1
            else :
                break
    if cnt :
        return cnt
    else :
        return -1

print(solution([1, 1, 2, 3, 3, 2, 2]))