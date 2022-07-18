num1 = int(input())
num2 = int(input())
sum = 0
count = 1
while num2 :
    sum += num1 * (num2 % 10) * count
    print(num1 * (num2 % 10))
    num2 = int(num2/10)
    count *= 10
print(sum)