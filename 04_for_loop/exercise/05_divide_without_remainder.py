n = int(input())
p1 = 0
p2 = 0
p3 = 0
for i in range(n):
    number = int(input())
    if number % 2 == 0:
        p1 += 1
    if number % 3 == 0:
        p2 += 1
    if number % 4 == 0:
        p3 += 1
p1_p = p1 / n * 100
p2_p = p2 / n * 100
p3_p = p3 / n * 100
print(f"{p1_p:.2f}%\n{p2_p:.2f}%\n{p3_p:.2f}%")
