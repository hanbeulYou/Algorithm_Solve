from collections import deque

def solution(n, m, x, y, r, c, k):
    move = ['d', 'l', 'r', 'u']
    direction = [(1, 0), (0, -1), (0, 1), (-1, 0)]
    queue = deque()
    queue.append((x, y, '', 0))
    answer = ''
    while queue:
        now_x, now_y, route, distance = queue.popleft()
        if distance == k:
            if (now_x, now_y) == (r, c):
                if answer == '' or answer > route:
                    answer = route
            continue
        
        for d in range(4):
            new_x = now_x + direction[d][0]
            new_y = now_y + direction[d][1]
            if 1 <= new_x <= n and 1 <= new_y <= m:
                queue.append((new_x, new_y, route+move[d], distance+1))

    if answer == '':
        answer = 'impossible'
    return answer

# print(solution(3, 4, 2, 3, 3, 1, 5))
print(solution(2, 2, 1, 1, 2, 2, 2))