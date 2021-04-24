chicken = int(input())
fish = int(input())
vegan = int(input())

chicken_price = 10.35
fish_price = 12.40
vegan_price = 8.15
total = chicken * chicken_price + fish * fish_price + vegan * vegan_price
total = total + total * 0.2 + 2.5
print(f"Total: {total:.2f}")
