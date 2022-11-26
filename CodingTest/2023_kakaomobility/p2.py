from collections import defaultdict

def solution(id_list, k):
    coupon = defaultdict(int)
    for id_item in id_list:
        day_ids_array = id_item.split(' ')
        day_ids = set(day_ids_array)
        for day_id in day_ids:
            coupon[day_id] += 1

    answer = 0    
    for key, value in coupon.items():
        answer += min(value, k)

    return answer

print(solution(["A B C D", "A D", "A B D", "B D"], 2))
print(solution(["JAY", "JAY ELLE JAY MAY", "MAY ELLE MAY", "ELLE MAY", "ELLE ELLE ELLE", "MAY"], 3))