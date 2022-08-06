def hanoi(fr, to, disk) :
    if disk == 1 :
        print(fr, to)
        return
    
    hanoi(fr, 6-fr-to, disk-1)
    print(fr, to)
    hanoi(6-fr-to, to, disk-1)

n = int(input())
print(2**n-1)
hanoi(1, 3, n)