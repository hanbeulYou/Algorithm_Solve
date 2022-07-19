import sys
sys.setrecursionlimit(10**5)

def stack_dice(bottom, floor, dice_sum) :
    global dice
    global n
    global max_sum

    if floor == n :
        if max_sum < dice_sum :
            max_sum = dice_sum
        return

    idx = dice[floor].index(bottom)
    tmp = dice[floor].copy()

    if idx == 0 :
        next_bottom = dice[floor][5]
        del tmp[0]
        del tmp[4]
        dice_sum += max(tmp)
        stack_dice(next_bottom, floor + 1, dice_sum)

    elif idx == 1 :
        next_bottom = dice[floor][3]
        del tmp[1]
        del tmp[2]
        dice_sum += max(tmp)
        stack_dice(next_bottom, floor + 1, dice_sum)

    elif idx == 2 :
        next_bottom = dice[floor][4]
        del tmp[2]
        del tmp[3]
        dice_sum += max(tmp)
        stack_dice(next_bottom, floor + 1, dice_sum)

    elif idx == 3 :
        next_bottom = dice[floor][1]
        del tmp[1]
        del tmp[2]
        dice_sum += max(tmp)
        stack_dice(next_bottom, floor + 1, dice_sum)
        
    elif idx == 4 :
        next_bottom = dice[floor][2]
        del tmp[2]
        del tmp[3]
        dice_sum += max(tmp)
        stack_dice(next_bottom, floor + 1, dice_sum)

    else :
        next_bottom = dice[floor][0]
        del tmp[0]
        del tmp[4]
        dice_sum += max(tmp)
        stack_dice(next_bottom, floor + 1, dice_sum)


n = int(input())
dice = [[0 for i in range(6)] for j in range(n)]

for dice_num in range(n) :
    dice[dice_num] = list(map(int, sys.stdin.readline().split()))

max_sum = 0
for i in range(6) :
    dice_sum = stack_dice(dice[0][i], 0, 0)

print(max_sum)