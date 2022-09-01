#5658_보물상자 비밀번호
#2022-08-19

T = int(input())
for tc in range(1, T+1) :
    N, K = map(int, input().split())
    words = list(input())
    word_len = N // 4
    values = set()
    for _ in range(word_len) :
        for i in range(0, N, word_len) :
            new_word = '0x'
            for j in range(word_len) :
                new_word += words[i+j]
            values.add(int(new_word, 16))
        change_word = words.pop()
        words.insert(0, change_word)

    arr = []
    for value in values :
        arr.append(value)
    arr.sort(reverse=True)
    print('#{} {}'.format(tc, arr[K-1]))