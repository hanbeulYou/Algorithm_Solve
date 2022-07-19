n = int(input())

new = n
flag = 1
count = 0

while 1 :
    ten = new // 10
    one = new % 10

    if new == n :
        if flag :
            flag = 0
        else :
            break

    new = (ten + one) % 10 + (new % 10) * 10
    count += 1

print(count)