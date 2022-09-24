def is_valid(alpha_arr):
    cnt_v = cnt_c = 0
    for alpha in alpha_arr:
        if alpha in vowels: cnt_v += 1
        else: cnt_c += 1
    if cnt_v >= 1 and cnt_c >= 2:
        return True
    return False


def dfs(idx, depth):
    if depth == L:
        if is_valid(password):
            print(''.join(password))
        return

    for i in range(idx+1, C):
        password[depth] = arr[i]
        dfs(i, depth+1)


vowels = ['a', 'e', 'i', 'o', 'u',]
L, C = map(int, input().split())
arr = list(input().split())
arr.sort()
password = [0]*L
dfs(-1, 0)