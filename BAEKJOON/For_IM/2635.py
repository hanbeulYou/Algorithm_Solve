n = int(input())

max_list = []
max_n = 0

for i in range(1, n + 1) :
    num_list = [n, i]
    num1 = n
    num2 = i
    while num1 - num2 >= 0 :
        num1, num2 = num2, num1 - num2
        num_list.append(num2)
    if max_n < len(num_list) :
        max_n = len(num_list)
        max_list = num_list.copy()
        
print (max_n)
for num in max_list :
    print(num, end=' ')