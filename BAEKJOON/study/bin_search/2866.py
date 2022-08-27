def cut(m):
    str_set = set()
    new_str = ['' for _ in range(C)]
    for j in range(C):
        for i in range(m, R):
            new_str[j] += arr[i][j]
        str_set.add(new_str[j])

    if len(str_set) == C:
        return True
    else:
        return False

R, C = map(int, input().split())
arr = list()
for _ in range(R):
    arr.append(input())

s, e = 0, R-1 
result = 0
while s <= e:
    m = (s+e)//2
    flag = cut(m)
    if flag:
        result = m
        s = m + 1
    else:
        e = m - 1
print(result)