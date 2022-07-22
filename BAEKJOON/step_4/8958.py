T = int(input())

for test_case in range(T) :
    quiz = input()
    len_quiz = len(quiz)
    score = [0 for _ in range(len_quiz)] 
    for idx, ox in enumerate(quiz) :
        if idx == 0 and ox == 'O' :
            score[idx] = 1
        elif ox =='O' :
            score[idx] = score[idx - 1] + 1
    print(sum(score))