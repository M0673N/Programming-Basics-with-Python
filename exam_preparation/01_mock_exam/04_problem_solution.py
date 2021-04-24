days = int(input())
food = float(input())
total_cat = 0
total_dog = 0
total_biscuits = 0
for day in range(1, days + 1):
    dog = int(input())
    cat = int(input())
    if day % 3 == 0:
        total_biscuits += cat * 0.1
        total_biscuits += dog * 0.1
    total_cat += cat
    total_dog += dog
print(f"Total eaten biscuits: {total_biscuits:.0f}gr.\n"
      f"{(total_dog + total_cat) / food * 100:.2f}% of the food has been eaten.\n"
      f"{total_dog / (total_dog + total_cat) * 100:.2f}% eaten from the dog.\n"
      f"{total_cat / (total_dog + total_cat) * 100:.2f}% eaten from the cat.")
