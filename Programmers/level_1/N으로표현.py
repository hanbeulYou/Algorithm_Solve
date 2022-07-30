# DP의 개념을 활용하긴 했지만 너무 지저분

def solution(N, number):
    cases = [[N]]
    number_idx = [-1 for _ in range(32001)] # 각각의 숫자가 몇번째 만에 계산되는지 저장하는 list
    number_idx[N] = 1

    for n in range(1, 9) :
        cases.append([])
        if int(str(N) * (n + 1)) <= 32000 : # 'N' 'NN' 'NNN' 등의 숫자 먼저 넣어줌
            if number_idx[int(str(N) * (n + 1))] == -1 :
                cases[n].append(int(str(N) * (n + 1)))
                number_idx[int((str(N) * (n + 1)))] = n + 1

        for i in range(0, (n // 2) + 1) : 
            for case_1 in cases[i] : # 0 ~ n/2 번까지
                for case_2 in cases[n - 1 - i] : # n/2 ~ n-1번까지

                    if case_1 + case_2 <= 32000 : # 합
                        if number_idx[case_1 + case_2] == - 1 :
                            cases[n].append(case_1 + case_2)
                            number_idx[case_1 + case_2] = n + 1

                    if case_1 * case_2 <= 32000 : # 곱
                        if number_idx[case_1 * case_2] == - 1 :
                            cases[n].append(case_1 * case_2)
                            number_idx[case_1 * case_2] = n + 1

                    if  case_1 != case_2 : # 차
                        if number_idx[abs(case_1 - case_2)] == - 1 :
                            cases[n].append(abs(case_1 - case_2))
                            number_idx[abs(case_1 - case_2)] = n + 1

                    if case_1 % case_2 == 0 : # 나누기
                        if number_idx[abs(case_1 // case_2)] == - 1 :
                            cases[n].append(case_1 // case_2)
                            number_idx[abs(case_1 // case_2)] = n + 1

                    if case_2 % case_1 == 0 :
                        if number_idx[abs(case_2 // case_1)] == - 1 :
                            cases[n].append(case_2 // case_1)
                            number_idx[abs(case_2 // case_1)] = n + 1

    return number_idx[number]

#print(solution(5, 55))