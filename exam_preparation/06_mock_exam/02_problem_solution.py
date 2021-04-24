guests = int(input())
budget = int(input())
expenses_eggs = guests * 0.9
cozonacs = guests // 3
if guests % 3 != 0:
    cozonacs += 1
total_expenses = expenses_eggs + cozonacs * 4
if budget < total_expenses:
    print(f"Lyubo doesn't have enough money.\n"
          f"He needs {total_expenses - budget:.2f} lv. more.")
else:
    print(f"Lyubo bought {cozonacs} Easter bread and {guests * 2} eggs.\n"
          f"He has {budget - total_expenses:.2f} lv. left.")
