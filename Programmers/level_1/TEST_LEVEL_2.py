import math

def solution(str1, str2):
    str1_list = list()
    str2_list = list()

    for idx in range(len(str1) - 1) :
        if str1[idx].isalpha() and str1[idx + 1].isalpha() :
            str1_list.append(str1[idx].upper() + str1[idx+1].upper())
    for idx in range(len(str2) - 1) :
        if str2[idx].isalpha() and str2[idx + 1].isalpha() :
            str2_list.append(str2[idx].upper() + str2[idx+1].upper())
    
    inter = []
    union = []

    for element_1 in str1_list :
        if element_1 in str2_list and element_1 not in inter :
            cnt1 = str1_list.count(element_1)
            cnt2 = str2_list.count(element_1)
            if cnt1 > cnt2 :
                for _ in range(cnt2) :
                    inter.append(element_1)
                for _ in range(cnt1) :
                    union.append(element_1)
            else :
                for _ in range(cnt1) :
                    inter.append(element_1)
                for _ in range(cnt2) :
                    union.append(element_1)
        elif element_1 not in str2_list :
            union.append(element_1)

    for element_2 in str2_list :
        if element_2 not in str1_list :
            union.append(element_2)

    if len(union) == 0 :
        return 65536
    return math.floor(len(inter) / len(union) * 65536)

print(solution("E=M*C^2", "e=m*c^2"))