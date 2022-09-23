def solution(id_list, reports, k):
    answer = [0 for _ in range(len(id_list))]
    to_report = dict()
    from_report = dict()
    
    for id_item in id_list:
        to_report[id_item] = []
        from_report[id_item] = []
    for report in reports:
        from_r, to_r = report.split()
        if from_r not in to_report[to_r]:
            to_report[to_r].append(from_r)
    
    for id_item in id_list:
        if len(to_report[id_item]) >= k:
            for from_r in to_report[id_item]:
                answer[id_list.index(from_r)] += 1

    return answer

print(solution(["con", "ryan"], ))