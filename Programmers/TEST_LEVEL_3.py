def dfs(node, cnt) :
    global visited
    global computers
    global n

    visited[node] = cnt
    for i in range(n) :
        if computers[node][i] and visited[i] == 0 :
            dfs(node, cnt)

def solution(n, computers):
    visited = [0 for _ in range(n)]
    stack = []
    cnt = 1
    for i in range(n) :
        if visited[i] == 0 :
            stack.append(i)
            while stack :
                node = stack.pop()
                visited[node] = cnt
                for j in range(n) :
                    if computers[node][j] and visited[j] == 0 :
                        stack.append(j)
            cnt+= 1
                
    return cnt - 1

print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))


"""def solution(n, money):
    pay_1 = [0 for _ in range(n+1)]
    for idx, m in enumerate(money) :
        i = m
        if idx == 0 :
            while i <= n :
                pay_1[i] += 1
                i += m
        
        else :
            pay_2 = pay_1[:]
            pay_2[0] = 1
            while i <= n :
                pay_2[i] = pay_1[i] + pay_2[i-m]
                i += 1
            pay_1 = pay_2[:]

    return pay_1[n]

print(solution(6, [4, 5]) % 1000000007)
"""