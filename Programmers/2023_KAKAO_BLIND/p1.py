from collections import defaultdict

def change_to_time(date):
    year, month, day = date.split('.')
    return int(year)*28*12 + int(month)*28 + int(day)

def solution(today, terms, privacies):
    today_time = change_to_time(today)
    terms_dict = defaultdict(int)

    for term in terms:
        privacy, privacy_term = term.split()
        terms_dict[privacy] = today_time - int(privacy_term)*28

    answer = []
    for idx, privacy in enumerate(privacies):
        privacy_time, privacy_type = privacy.split()
        privacy_time = change_to_time(privacy_time)
        if privacy_time <= terms_dict[privacy_type]:
            answer.append(idx+1)

    return answer

print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))