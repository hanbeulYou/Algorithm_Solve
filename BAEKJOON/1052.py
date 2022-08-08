n, k = map(int, input().split())
cnt = 0

# cnt개의 물병을 구매했을 때 2^x k개로 n을 표현 가능
# 2진법을 사용해 표현.
while k < bin(n).count('1'):
    n += 1
    cnt += 1

print(cnt)