change = float(input())
coin_counter = 0
while round(change, 2) > 0:
    coin_counter += 1
    if round(change, 2) - 2 >= 0:
        change -= 2
    elif round(change, 2) - 1 >= 0:
        change -= 1
    elif round(change, 2) - 0.5 >= 0:
        change -= 0.5
    elif round(change, 2) - 0.2 >= 0:
        change -= 0.2
    elif round(change, 2) - 0.1 >= 0:
        change -= 0.1
    elif round(change, 2) - 0.05 >= 0:
        change -= 0.05
    elif round(change, 2) - 0.02 >= 0:
        change -= 0.02
    elif round(change, 2) - 0.01 >= 0:
        change -= 0.01
print(coin_counter)
