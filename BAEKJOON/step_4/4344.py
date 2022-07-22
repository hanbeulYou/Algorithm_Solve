C = int(input())

for test_case in range(C) :
    scores = list(map(int, input().split()))
    N = scores[0]
    del(scores[0])
    score_avg = sum(scores) / N
    cnt = 0
    for score in scores :
        if score > score_avg :
            cnt += 1
    cnt_percent = cnt / N * 100
    cnt_percent = round(cnt_percent, 3)
    print('{:.3f}%'.format(cnt_percent))