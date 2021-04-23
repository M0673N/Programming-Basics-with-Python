from sys import maxsize

n = int(input())
odd_highest = -maxsize
even_highest = -maxsize
odd_min = maxsize
even_min = maxsize
odd_sum = 0
even_sum = 0
counter = 0
for i in range(n):
    counter += 1
    num = float(input())
    if counter % 2 == 1:
        odd_sum += num
        if num > odd_highest:
            odd_highest = num
        if num < odd_min:
            odd_min = num
    elif counter % 2 == 0:
        even_sum += num
        if num > even_highest:
            even_highest = num
        if num < even_min:
            even_min = num

print(f"OddSum={odd_sum:.2f},")
if odd_min != maxsize:
    print(f"OddMin={odd_min:.2f},")
else:
    print(f"OddMin=No,")
if odd_highest != -maxsize:
    print(f"OddMax={odd_highest:.2f},")
else:
    print(f"OddMax=No,")
print(f"EvenSum={even_sum:.2f},")
if even_min == maxsize:
    print(f"EvenMin=No,")
else:
    print(f"EvenMin={even_min:.2f},")
if even_highest == -maxsize:
    print(f"EvenMax=No")
else:
    print(f"EvenMax={even_highest:.2f}")
