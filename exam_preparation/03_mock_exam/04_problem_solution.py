capacity = int(input())
line = input()
total_income = 0
people = 0
while line != "Movie time!":
    people += int(line)
    if people > capacity:
        print("The cinema is full.")
        break
    if int(line) % 3 == 0:
        total_income += int(line) * 5 - 5
    else:
        total_income += int(line) * 5
    if people > capacity:
        print("The cinema is full.")
        break
    line = input()
else:
    print(f"There are {capacity - people} seats left in the cinema.")
print(f"Cinema income - {total_income} lv.")
