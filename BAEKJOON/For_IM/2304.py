n = int(input())
pillars = {}

for i in range(n) :
    pillar_idx, pillar_height = map(int, input().split())
    pillars[pillar_idx] = pillar_height

left_idx = 0
left_height = 0
left_sum = 0

while left_height < max(pillars.values()) :
    if left_idx in pillars.keys() :
        if left_height < pillars[left_idx] :
            left_height = pillars[left_idx]
    left_sum += left_height
    left_idx += 1

right_idx = max(pillars.keys())
right_height = 0
right_sum = 0

while right_height < max(pillars.values()) :
    if right_idx in pillars.keys() :
        if right_height < pillars[right_idx] :
            right_height = pillars[right_idx]
    right_sum += right_height
    right_idx -= 1

print(left_sum + right_sum - ((left_idx - right_idx) - 1) * max(pillars.values()))
