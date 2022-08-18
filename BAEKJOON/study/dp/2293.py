N, K = map(int, input().split())
dp_1 = [0]*(K+1)
for i in range(N) :
    coin = int(input())
    dp_2 = [0]*(K+1)
    idx = 0

    if i == 0 :
        while idx <= K :
            dp_1[idx] += 1
            idx += coin
    
    else :
        while idx <= K :
            if idx < coin :
                dp_2[idx] = dp_1[idx]
            else :
                dp_2[idx] = dp_1[idx] + dp_2[idx-coin]
            idx += 1
        dp_1 = dp_2[:]

if N == 1 :
    print(dp_1[K])
else :
    print(dp_2[K])