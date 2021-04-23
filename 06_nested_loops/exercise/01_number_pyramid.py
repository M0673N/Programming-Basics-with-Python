n = int(input())
number = 1
for row in range(1, n + 1):
    for col in range(1, row + 1):
        if number == n + 1:
            break
        print(number, end=" ")
        number += 1
    if number == n + 1:
        break
    print()
