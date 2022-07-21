n, k = map(int, input().split())
temps = list(map(int, input().split()))

sum_temps = sum(temps[0:k])
len_temps = len(temps)
max_sum = sum_temps
for idx in range(k, len_temps) :
    sum_temps = sum_temps - temps[idx - k] + temps[idx]
    if max_sum < sum_temps :
        max_sum = sum_temps

print(max_sum)