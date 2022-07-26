def solution(id_list, reports, k):
    new_reports = []
    for report in reports :
        if report not in new_reports :
            new_reports.append(report)

    report_dict = {}
    report_id = {}
    reported_id = {}
    n = 0
    for ids in id_list :
        report_dict[ids] = []
        report_id[ids] = 0
        reported_id[ids] = 0
        n += 1
    
    for report in new_reports :
        report_from, report_to = report.split()
        report_dict[report_from].append(report_to)
        reported_id[report_to] += 1

    for key in reported_id.keys() :
        if reported_id[key] >= k :
            for dict_key, value_list in report_dict.items() :
                for value in value_list :
                    if key == value :
                        report_id[dict_key] += 1
    return_list = []
    for value in report_id.values() :
        return_list.append(value)
    return return_list
#    return report_dict

solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)