def solution(N, number):
    cases = [[N]]
    number_idx = {} # 각각의 숫자가 몇번째 만에 계산되는지 저장하는 dict
    number_idx[N] = 1
    for n in range(1, 9) :
        cases.append([])
        if int(str(N) * (n + 1)) : # 'N' 'NN' 'NNN' 등의 숫자 먼저 넣어줌
            cases[n].append(int(str(N) * (n + 1)))
            number_idx[int((str(N) * (n + 1)))] = n + 1

        for i in range(0, (n // 2) + 1) : # 0 ~ n/2 번까지
            for case_1 in cases[i] : 
                for case_2 in cases[n - 1 - i] : # i에 대한 반댓값 ?? n - i - 1번 째

                    if case_1 + case_2 : # 합
                        if case_1 + case_2 not in number_idx.keys() :
                            cases[n].append(case_1 + case_2)
                            number_idx[case_1 + case_2] = n + 1

                    if case_1 * case_2 : # 곱
                        if case_1 * case_2 not in number_idx.keys()  :
                            cases[n].append(case_1 * case_2)
                            number_idx[case_1 * case_2] = n + 1

                    if case_1 != case_2 : # 차
                        if abs(case_1 - case_2) not in number_idx.keys()  :
                            cases[n].append(abs(case_1 - case_2))
                            number_idx[abs(case_1 - case_2)] = n + 1

                    if case_1 % case_2 == 0 : # 나누기
                        if abs(case_1 // case_2) not in number_idx.keys() :
                            cases[n].append(case_1 // case_2)
                            number_idx[abs(case_1 // case_2)] = n + 1

                    if case_2 % case_1 == 0 : # 나누기
                        if abs(case_2 // case_1) not in number_idx.keys() :
                            cases[n].append(case_2 // case_1)
                            number_idx[abs(case_2 // case_1)] = n + 1

#        print(cases[n])
    return number_idx[number]

print(solution(5,11111))