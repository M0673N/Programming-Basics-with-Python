days = int(input())
hours = int(input())
counter = 1
counter2 = 1
total = 0
for day in range(days):
    day_price = 0
    counter2 = 1
    for hour in range(hours):
        if counter % 2 == 0 and counter2 % 2 == 1:
            day_price += 2.5
        elif counter % 2 == 1 and counter2 % 2 == 0:
            day_price += 1.25
        else:
            day_price += 1
        counter2 += 1
    print(f"Day: {counter} - {day_price:.2f} leva")
    counter += 1
    total += day_price
print(f"Total: {total:.2f} leva")
