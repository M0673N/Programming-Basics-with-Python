food = int(input()) * 1000
consumed = input()
total_consumed = 0
while consumed != "Adopted":
    total_consumed += int(consumed)
    consumed = input()
if total_consumed > food:
    print(f"Food is not enough. You need {total_consumed - food} grams more.")
else:
    print(f"Food is enough! Leftovers: {food - total_consumed} grams.")
