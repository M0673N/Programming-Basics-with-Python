n = int(input())
current_min = ""
current_max = ""
for i in range(n):
    number = int(input())
    if current_max == "" or number > current_max:
        current_max = number
    if current_min == "" or number < current_min:
        current_min = number
print(f"Max number: {current_max}")
print(f"Min number: {current_min}")
