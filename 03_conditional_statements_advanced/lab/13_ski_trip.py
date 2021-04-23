days = int(input())
type_of_room = input()
evaluation = input()
discount = False
price = (days - 1) * 18
final_price = price

if type_of_room == "apartment":
    price = (days - 1) * 25
    if days < 10:
        discount = price * 0.30
    if 10 <= days <= 15:
        discount = price * 0.35
    if 15 < days:
        discount = price * 0.50
    final_price = price - discount

if type_of_room == "president apartment":
    price = (days - 1) * 35
    if days < 10:
        discount = price * 0.10
    if 10 <= days <= 15:
        discount = price * 0.15
    if 15 < days:
        discount = price * 0.20
    final_price = price - discount

if evaluation == "positive":
    final_price = final_price + final_price * 0.25
if evaluation == "negative":
    final_price = final_price - final_price * 0.10

print(f"{final_price:.2f}")
