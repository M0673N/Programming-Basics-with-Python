budget = float(input())
season = input()

if budget <= 100:
    location = "Bulgaria"
    if season == "winter":
        expenses = budget * 0.7
        type_ = "Hotel"
    else:
        expenses = budget * 0.3
        type_ = "Camp"

if 100 < budget <= 1000:
    location = "Balkans"
    if season == "winter":
        expenses = budget * 0.8
        type_ = "Hotel"
    else:
        expenses = budget * 0.4
        type_ = "Camp"
if budget > 1000:
    location = "Europe"
    expenses = budget * 0.9
    type_ = "Hotel"

print(f"Somewhere in {location}")
print(f"{type_} - {expenses:.2f}")
