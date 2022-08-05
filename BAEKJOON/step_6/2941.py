alphas = list(input())

cnt = 0
n = len(alphas)
idx = 0

while idx < n :
    if alphas[idx] == 'c' and idx != n - 1 :
        if alphas[idx + 1] == '=' or alphas[idx + 1] == '-':
            cnt += 1
            idx += 2
            continue
        else :
            idx += 1
            cnt += 1
    elif alphas[idx] == 'd' and idx != n - 1 :
        if alphas[idx + 1] == '-':
            cnt += 1
            idx += 2
            continue
        elif idx != n - 2 :
            if alphas[idx + 1] =='z' and alphas[idx + 2] == '=' :
                cnt += 1
                idx += 3
                continue
            else :
                idx += 1
                cnt += 1
        else :
            idx += 1
            cnt += 1
    elif alphas[idx] == 'l' and idx != n - 1 :
        if alphas[idx + 1] == 'j' :
            cnt += 1
            idx += 2
            continue
        else :
            cnt += 1
            idx += 1
    elif alphas[idx] == 'n' and idx != n - 1 :
        if alphas[idx + 1] == 'j' :
            cnt += 1
            idx += 2
            continue
        else :
            cnt += 1
            idx += 1
    elif alphas[idx] == 's' and idx != n - 1 :
        if alphas[idx + 1] == '=' :
            cnt += 1
            idx += 2
            continue
        else :
            cnt += 1
            idx += 1
    elif alphas[idx] == 'z' and idx != n - 1 :
        if alphas[idx + 1] == '=' :
            cnt += 1
            idx += 2
            continue
        else :
            cnt += 1
            idx += 1
    else :
        cnt += 1
        idx += 1

print(cnt)