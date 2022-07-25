for test_case in range(1, 11) :
    n = int(input())
    dumps = list(map(int, input().split()))
    for _ in range(n) :
        max_dump = max(dumps)
        max_idx = dumps.index(max_dump)
        min_dump = min(dumps)
        min_idx = dumps.index(min_dump)
        
        dumps[max_idx] -= 1
        dumps[min_idx] += 1
        
    print('#{}'.format(test_case), max(dumps) - min(dumps))