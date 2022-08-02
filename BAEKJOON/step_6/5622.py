alphas = input()
dials = [3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10]
time = 0
for alpha in alphas :
    time += dials[ord(alpha) - 65]

print(time)