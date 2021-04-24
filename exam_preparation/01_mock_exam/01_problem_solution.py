BTC_PRICE = 1168
USD_PRICE = 1.76
CNY_PRICE = 0.15 * USD_PRICE
btc = int(input())
cny = float(input())
commission = float(input())
result = (BTC_PRICE * btc + CNY_PRICE * cny) / 1.95
result *= (1 - commission / 100)
print(f"{result:.2f}")
