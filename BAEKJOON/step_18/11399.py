n = int(input())
people = sorted(list(map(int, input().split())))
t = 0
for i in range(n):
    t += people[i] * (n - i)
print(t)