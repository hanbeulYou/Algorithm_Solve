for _ in range(4) :
    a_x1, a_y1, a_x2, a_y2, b_x1, b_y1, b_x2, b_y2 = map(int, input().split())
    if b_x1 > a_x2 or b_y1 > a_y2 :
        print('d')
        continue
    elif a_x1 > b_x2 or a_y1 > b_y2 :
        print('d')
        continue
    elif a_x1 == b_x2 and a_y1 == b_y2 :
        print('c')
        continue
    elif a_x2 == b_x1 and a_y1 == b_y2 :
        print('c')
        continue
    elif a_x2 == b_x1 and a_y2 == b_y1 :
        print('c')
        continue
    elif a_x1 == b_x2 and a_y2 == b_y1 :
        print('c')
        continue
    elif a_x1 == b_x2 or a_x2 == b_x1 :
        print('b')
        continue
    elif a_y1 == b_y2 or a_y2 == b_y1 :
        print('b')
        continue
    else :
        print('a')
        continue