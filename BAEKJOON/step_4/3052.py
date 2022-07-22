remainder_42 = [0 for _ in range(42)]
for _ in range(10) :
    n = int(input())
    remainder_42[n % 42] += 1

cnt = 0
for num in remainder_42 :
    if num != 0 :
        cnt += 1

print(cnt)