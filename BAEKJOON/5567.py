import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
friendship = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    friendship[a].append(b)
    friendship[b].append(a)
    
invited = [0 for _ in range(n+1)]

for friend in friendship[1]:
    invited[friend] = 1
    for new_friend in friendship[friend]:
        invited[new_friend] = 1
if sum(invited):
    print(sum(invited)-1)
else:
    print(0)