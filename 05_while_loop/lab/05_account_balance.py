command = 0
total = 0
while command != "NoMoreMoney":
    command = input()
    if command == "NoMoreMoney":
        break
    if float(command) >= 0:
        print(f"Increase: {(float(command)):.2f}")
        total += float(command)
    else:
        print("Invalid operation!")
        break
print(f"Total: {total:.2f}")
