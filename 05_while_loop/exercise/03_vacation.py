required = float(input())
balance = float(input())
spend_counter = 0
days = 0
while balance < required:
    operation_type = input()
    amount = float(input())
    if operation_type == "save":
        balance += amount
        spend_counter = 0
    elif operation_type == "spend":
        balance -= amount
        spend_counter += 1
        if balance < 0:
            balance = 0
    days += 1
    if spend_counter == 5:
        print("You can't save the money.")
        print(days)
        break
if balance >= required:
    print(f"You saved the money for {days} days.")
