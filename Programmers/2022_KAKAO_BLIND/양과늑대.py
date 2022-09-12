def solution(info, edges):
    n = len(info)
    answer = []
    visited = [False for _ in range(n)]
    visited[0] = True

    def dfs(s, w):
        if s > w:
            answer.append(s)
        else:
            return
    
        for edge in edges:
            if visited[edge[0]] and not visited[edge[1]]:
                visited[edge[1]] = True
                if info[edge[1]] == 1:
                    dfs(s, w+1)
                else:
                    dfs(s+1, w)
                visited[edge[1]] = False
    
    dfs(1, 0)

    return max(answer)

# print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
print(solution([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))