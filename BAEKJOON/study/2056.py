N = int(input())
graph = [[] for _ in range(N+1)]
times = [0 for _ in range(N+1)]
for i in range(1, N+1):
    input_arr = list(map(int, input().split()))
    times[i] = input_arr[0]
    if input_arr[1]:
        max_time = 0
        for j in input_arr[2:]:
            max_time = max(max_time, times[j])
        times[i] += max_time

print(max(times))