film = input()
package = input()
tickets = int(input())
if film == "John Wick":
    if package == "Drink":
        price = 12
    elif package == "Popcorn":
        price = 15
    else:
        price = 19
elif film == "Star Wars":
    if package == "Drink":
        price = 18
    elif package == "Popcorn":
        price = 25
    else:
        price = 30
else:
    if package == "Drink":
        price = 9
    elif package == "Popcorn":
        price = 11
    else:
        price = 14
if film == "Star Wars" and tickets >= 4:
    price *= 0.7
if film == "Jumanji" and tickets == 2:
    price *= 0.85
print(f"Your bill is {price * tickets:.2f} leva.")
