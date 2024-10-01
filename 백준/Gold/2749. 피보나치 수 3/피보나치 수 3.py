MAX_NUM = 1500000
INF = 1000000

n = int(input())
P = [0 for _ in range(MAX_NUM+2)]

P[0] = 0
P[1] = 1

for i in range(MAX_NUM):
    P[i+2] = (P[i] + P[i+1]) % INF

print(P[n % MAX_NUM])