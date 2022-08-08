import sys
while True :
    try :
        x = int(input())
        x *= 10000000
        n = int(input())
        legos = []
        for _ in range(n) :
            lego = int(input())
            if lego >= x :
                continue
            else :
                legos.append(lego)
        legos.sort()
        n = len(legos)
        s_idx = 0
        e_idx = n - 1

        yes = True
        while s_idx < e_idx :
            if legos[s_idx] + legos[e_idx] == x :
                print(f'yes {legos[s_idx]} {legos[e_idx]}')
                break
            if legos[s_idx] + legos[e_idx] < x :
                s_idx += 1

            else :
                if e_idx - 1 > 0 :
                    if s_idx == 0 :
                        print('danger')
                        yes = False
                        break
                    else :
                        while legos[s_idx] + legos[e_idx - 1] >= x :
                            s_idx -= 1
                        e_idx -= 1
                        continue
                else :
                    yes = False
                    print('danger')
                    break
        if yes :
            print('danger')
            
    except EOFError :
        break