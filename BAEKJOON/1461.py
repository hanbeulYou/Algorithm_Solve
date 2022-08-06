n, m = map(int, input().split())
locs = list(map(int, input().split()))

positive = []
negative = []
length = 0

# 양수와 음수를 각각의 list에 append 해줌
for loc in locs :
    if loc > 0 :
        positive.append(loc)
    else :
        negative.append(abs(loc))

# list sorting(idx 계산 쉽게 하기 위해 내림차순으로 함)
positive.sort(reverse=True)
negative.sort(reverse=True)

# list 안의 요소들을 삭제할거라 미리 최댓값을 구해서 제외해놓음
length -= max(max(positive, negative))

len_p = len(positive)
len_n = len(negative)

# 각 list별 (m개 요소 묶음별 최장거리 * 2)를 더해줌
while len_p >= m :
    length += positive[0] * 2
    len_p -= m
    del positive[0:m]

if len_p != 0 :
    length += positive[0] * 2

while len_n >= m :
    length += negative[0] * 2
    len_n -= m
    del negative[0:m]

if len_n != 0 :
    length += negative[0] * 2

print(length)