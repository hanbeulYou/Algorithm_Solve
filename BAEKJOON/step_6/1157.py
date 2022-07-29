alphabets = list(input().lower())

cnt = [0 for _ in range(26)]
for alpha in alphabets :
    cnt[ord(alpha) - 97] += 1
idx = -1
flag = 1
for i in range(26) :
    if max(cnt) == cnt[i] :
        if idx == - 1 :
            idx = i
        else :
            flag = 0
            print('?')
            break

if flag :
    print(chr(idx + 65))