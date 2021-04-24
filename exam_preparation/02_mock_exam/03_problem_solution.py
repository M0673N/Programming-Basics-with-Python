term = input()
contract_type = input()
mobile_internet = input()
months = int(input())
if term == "one":
    if contract_type == "Small":
        price = 9.98
    elif contract_type == "Middle":
        price = 18.99
    elif contract_type == "Large":
        price = 25.98
    else:
        price = 35.99
else:
    if contract_type == "Small":
        price = 8.58
    elif contract_type == "Middle":
        price = 17.09
    elif contract_type == "Large":
        price = 23.59
    else:
        price = 31.79
if mobile_internet == "yes":
    if price > 30:
        price = price + 3.85
    elif price <= 10:
        price = price + 5.5
    else:
        price = price + 4.35
if term == "two":
    price *= 0.9625
print(f"{(price * months):.2f} lv.")
