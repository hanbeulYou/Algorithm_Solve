T = int(input())
for test_case in range(T) :
    R, S = input().split()
    S = list(S)
    for c in S :
        print(c * int(R), end ='')
    print()