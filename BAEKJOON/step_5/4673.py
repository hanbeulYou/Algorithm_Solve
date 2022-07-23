num_list = [0 for _ in range(10001)]

def sum_digit(n) :
    if n > 9 :
        return n % 10 + sum_digit(n//10)
    else :
        return n % 10

def d(n) :
    global num_list
    if n + sum_digit(n) <= 10000 :
        num_list[n + sum_digit(n)] = 1

for num in range(1, 10001) :
    d(num)

for num in range(1, 10001) :
    if num_list[num] == 0 :
        print(num)