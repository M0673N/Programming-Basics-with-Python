square_meters = float(input())
price = square_meters * 7.61
discount = price * 18 / 100
final_price = price - price * 18 / 100
print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")
