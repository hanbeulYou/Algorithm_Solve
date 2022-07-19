n, x = map(int,input().split())
arr = [0 for i in range(n)]

arr = list(map(int,input().split()))

for i in range(n) :
    if arr[i] < x :
        print(arr[i], end =' ')