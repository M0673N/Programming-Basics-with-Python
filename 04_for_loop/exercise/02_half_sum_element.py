import sys

n = int(input())
total = 0
highest = -sys.maxsize
for i in range(n):
    number = int(input())
    total += number
    if number > highest:
        highest = number
if total / 2 == highest:
    print(f"Yes\nSum = {(total / 2):.0f}")
else:
    print(f"No\nDiff = {abs(highest - (total - highest))}")
