n = int(input())
w_machine = float(input())
doll_price = int(input())
dolls = 0
gift = 0
sibling_theft = 0
total_money = 0
for i in range(1, n+1):
    if i % 2 == 1:
        dolls += 1
    if i % 2 == 0:
        gift += 10
        total_money += gift
        sibling_theft += 1
total_money -= sibling_theft
doll_bonus = dolls * doll_price
total_money += doll_bonus
if total_money >= w_machine:
    print(f"Yes! {(total_money - w_machine):.2f}")
else:
    print(f"No! {(w_machine - total_money):.2f}")
