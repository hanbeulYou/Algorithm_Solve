n = int(input())
pick = list(map(int, input().split()))
line = [0 for _ in range(n)]

for number in range(1, n + 1) :
    idx = (number - 1) - pick[number - 1]
    for i in range(n - 1, idx, -1) :
        line[i] = line[i - 1]
    line[idx] = number

for idx, student in enumerate(line) :
    if idx == len(line) - 1 :
        print(student, end ='')
    else : 
        print(student, end =' ')