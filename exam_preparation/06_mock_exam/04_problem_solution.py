eggs = int(input())
action = input()
sold_eggs = 0
while action != "Close":
    number = 0
    if action == "Buy":
        number = int(input())
        eggs -= number
    else:
        eggs += int(input())
    sold_eggs += number
    if eggs < 0:
        print(f"Not enough eggs in store!\n"
              f"You can buy only {eggs + number}.")
        break
    action = input()
else:
    print(f"Store is closed!\n"
          f"{sold_eggs} eggs sold.")
