import sys

N = int(sys.stdin.readline())

for _ in range(N) :
    scabs_A = list(map(int, sys.stdin.readline().split()))
    scabs_B = list(map(int, sys.stdin.readline().split()))
    cnt_A = [0 for _ in range(5)]
    cnt_B = [0 for _ in range(5)]
    
    del(scabs_A[0])
    del(scabs_B[0])
    
    for scab in scabs_A :
        cnt_A[scab] += 1
    for scab in scabs_B :
        cnt_B[scab] += 1
        
    if cnt_A[4] != cnt_B[4] :
        winner = 'A' if cnt_A[4] > cnt_B[4] else 'B'
        print(winner)
        
    else :
        if cnt_A[3] != cnt_B[3] :
            winner = 'A' if cnt_A[3] > cnt_B[3] else 'B'
            print(winner)
        
        else :
            if cnt_A[2] != cnt_B[2] :
                winner = 'A' if cnt_A[2] > cnt_B[2] else 'B'
                print(winner)
                
            else :
                if cnt_A[1] != cnt_B[1] :
                    winner = 'A' if cnt_A[1] > cnt_B[1] else 'B'
                    print(winner)
                    
                else :
                    winner = 'D'
                    print(winner)