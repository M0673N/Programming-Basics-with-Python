budget = float(input())
price = 0
counter = 0
while True:
    line = input()
    if line == "Stop":
        break
    counter += 1
    if counter % 3 == 0:
        product = (float(input())) * 0.5
    else:
        product = float(input())
    price += product
    if price > budget:
        break
if line == "Stop":
    print(f"You bought {counter} products for {price:.2f} leva.")
else:
    print(f"You don't have enough money!\nYou need {(price - budget):.2f} leva!")
