price = int(input())
shoes = price * 0.6
suit = shoes * 0.8
ball = suit / 4
accessories = ball / 5
print(f"{price + shoes + suit + ball + accessories:.2f}")
