guests = int(input())
price = float(input())
budget = float(input())
if 10 <= guests <= 15:
    price *= 0.85
elif 15 < guests <= 20:
    price *= 0.8
elif 20 < guests:
    price *= 0.75
cake = budget * 0.1
if budget > price * guests + cake:
    print(f"It is party time! {budget - (price * guests + cake):.2f} leva left.")
else:
    print(f"No party! {abs(budget - (price * guests + cake)):.2f} leva needed.")
