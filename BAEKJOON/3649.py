import sys

while True :
    try :
        x = int(sys.stdin.readline())
        x *= 10000000
        n = int(sys.stdin.readline())
        legos = []
        for _ in range(n) :
            lego = int(sys.stdin.readline())
            if lego >= x :
                continue
            else :
                legos.append(lego)
                
        legos.sort()
        n = len(legos)
        s_idx = 0
        e_idx = n - 1
        
        while s_idx < e_idx :
            sum_lego = legos[s_idx] + legos[e_idx]
            
            if sum_lego > x :
                e_idx -= 1
            
            elif sum_lego < x :
                s_idx += 1
                
            else :
                print(f'yes {legos[s_idx]} {legos[e_idx]}')
                break
        else :
            print('danger')
            
    except :
        break