n = int(input())
cnt = 0
for _ in range(n) :
    string = list(input())
    idx = 0
    while idx < len(string) - 1 :
        if string[idx] == string[idx + 1] :
            del string[idx + 1]
        else :
            idx += 1
    if len(string) == len(set(string)) :
        cnt += 1
print(cnt)