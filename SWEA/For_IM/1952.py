#1952_수영장 풀이
#2022-08-18

# 3개월 최솟값 찾기
def three(new_paid, new_pay) :
    global pay
    pay = min(pay, new_pay)
    for i in range(12) :
        flag = 1
        change_pay = 0
        num = 3 if i < 10 else 12 - i
        for j in range(num) :
            if new_paid[i+j] == 'd' : 
                change_pay += attendance[i+j] * day
            if new_paid[i+j] == 'm' :
                change_pay += month
            if new_paid[i+j] == 't':
                flag = 0
        if flag :
            if new_pay > new_pay - change_pay + three_month :
                memory = []
                for j in range(i, i+3) :
                    if j == 12 : break
                    memory.append(new_paid[j])
                    new_paid[j] = 't'
                three(new_paid, new_pay - change_pay + three_month) 
                # 다녀온 곳 다시 초기화
                for j in range(i, i+3) :
                    if j == 12 : break
                    new_paid[j] = memory[j-i]


T = int(input())
for tc in range(1, T+1) :
    day, month, three_month, year = map(int, input().split())
    attendance = list(map(int, input().split()))
    paid = [0 for _ in range(12)]
    pay = 0

    # 1일 요금제로 끊었을 때
    for idx in range(12) :
        if attendance[idx] != 0 :
            paid[idx] = 'd'
            pay += attendance[idx] * day

    # 1일 + 1개월 요금제
    for idx in range(12) :
        if pay > pay - (day * attendance[idx]) + month :
            pay = pay - (day * attendance[idx]) + month
            paid[idx] = 'm'

    # 1일 + 1개월 + 3개월 요금제
    three(paid, pay)
    
    pay = min(pay, year)
    print('#{} {}'.format(tc, pay))