hour, minute = map(int, input().split())

if minute >= 45 :
    print(hour, minute - 45)
else :
    if hour > 0 :
        print(hour - 1, minute + 15)
    else :
        print(23, minute + 15)