import sys
import math

n, k = map(int, sys.stdin.readline().split())
students = [[0 for _ in range(2)] for _ in range(6)]

for _ in range(n) :
    s, y = map(int,sys.stdin.readline().split())
    students[y - 1][s] += 1

room = 0
for i in range(6) :
    for j in range(2) :
        if(students[i][j] == 0) :
            continue
        room += math.ceil(students[i][j] / k)
        
print(room)