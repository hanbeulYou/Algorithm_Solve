from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    n1 = sum(queue1)
    n2 = sum(queue2)
    if (n1+n2)%2:
        return -1
    cnt = 0
    while True:
        if n1 == n2:
            return cnt
        elif n1>n2:
            tmp = queue1.popleft()
            n1 -= tmp
            n2 += tmp
            queue2.append(tmp)
        else:
            tmp = queue2.popleft()
            n1 += tmp
            n2 -= tmp
            queue1.append(tmp)
        cnt += 1
        if cnt == (len(queue1)+len(queue2)) * 2:
            return -1


#print(solution([3, 2, 7, 2], [4, 6, 5, 1],))
#print(solution([1, 2, 1, 2], [1, 10, 1, 2],))
print(solution([1,1], [1,5]))