n, k = map(int, input().split())
coins = []

for _ in range(n) :
    coins.append(int(input()))

coins.sort(reverse=True)
cnt = 0
while k != 0 :
    for coin in coins :
        if k >= coin :
            k -= coin
            cnt += 1
            break
        if k < coin :
            del coin

print(cnt)