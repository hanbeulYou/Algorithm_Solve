def solution(steps_one, names_one, steps_two, names_two, steps_three, names_three):
    manbo_1 = {}
    manbo_2 = {}
    manbo_3 = {}
    manbo = {}

    for idx, name in enumerate(names_one) :
        if name not in manbo_1.keys() :
            manbo[name] = 0
            manbo_1[name] = []
        manbo_1[name].append(steps_one[idx])
        
    for idx, name in enumerate(names_two) :
        if name not in manbo_2.keys() :
            manbo[name] = 0
            manbo_2[name] = []
        manbo_2[name].append(steps_two[idx])

    for idx, name in enumerate(names_three) :
        if name not in manbo_3.keys() :
            manbo[name] = 0
            manbo_3[name] = []
        manbo_3[name].append(steps_three[idx])
    
    for key in manbo_1.keys() :
        manbo[key] += max(manbo_1[key])
    for key in manbo_2.keys() :
        manbo[key] += max(manbo_2[key])
    for key in manbo_3.keys() :
        manbo[key] += max(manbo_3[key])
    
    sorted_manbo = sorted(manbo.items(), key=lambda x: x[1], reverse=True)
    n = len(sorted_manbo)
    idx = 0

    while idx < n - 1 :
        if sorted_manbo[idx][1] == sorted_manbo[idx+1][1] :
            if sorted_manbo[idx][0] > sorted_manbo[idx+1][0] :
                sorted_manbo[idx], sorted_manbo[idx+1] = sorted_manbo[idx+1], sorted_manbo[idx]
                idx = 0
            else :
                idx += 1
        else :
            idx += 1
    
    manbo_list = []
    for m in sorted_manbo :
        manbo_list.append(m[0])
    return manbo_list

print(solution([1,2,3,4,5,6],["j","b","a","j","b","a"],[10,20,30,1,1,1,8],["j", "a", "b","d","d","d","d",],[1000,1,1,27,7],["b","a","j","c","d"]))