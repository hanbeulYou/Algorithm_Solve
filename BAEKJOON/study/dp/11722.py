N = int(input())
seq = list(map(int, input().split()))
max_lens = [0] * (N+1)
seq.append(0)

for idx in range(N-1, -1, -1) :
    max_len = 0
    for j in range(idx+1, N+1) :
        if seq[idx] > seq[j] :
            max_len = max(max_len, max_lens[j] + 1)
    max_lens[idx] = max_len

print(max(max_lens))