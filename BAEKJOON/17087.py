import math
N, S = map(int, input().split())
A_list = sorted(list(map(lambda a : abs(int(a) - S), input().split())))
g = A_list[0]
for i in range(1, N) :
    g = math.gcd(g, A_list[i])
print(g)