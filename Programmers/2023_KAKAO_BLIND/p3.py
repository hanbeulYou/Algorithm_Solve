def solution(users, emoticons):
    global max_cnt
    global max_revenue
    sales = [40, 30, 20, 10]

    n = len(emoticons)
    emo_sales = [0 for _ in range(n)]
    max_cnt, max_revenue = 0, 0


    def dfs(depth):
        global max_cnt
        global max_revenue
        
        if depth == n:
            cnt = 0
            revenue = 0
            for user in users:
                user_buy = 0
                for idx, emo_sale in enumerate(emo_sales):
                    if emo_sale >= user[0]:
                        user_buy += emoticons[idx] * (100-emo_sale) // 100
                if user_buy >= user[1]:
                    cnt += 1
                else:
                    revenue += user_buy
            if max_cnt < cnt:
                max_cnt = cnt
                max_revenue = revenue
            elif max_cnt == cnt and max_revenue < revenue:
                max_revenue = revenue
            return
    
        for sale in sales:
            emo_sales[depth] = sale
            dfs(depth+1)
    
    dfs(0)

    answer = [max_cnt, max_revenue]
    return answer

# print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))