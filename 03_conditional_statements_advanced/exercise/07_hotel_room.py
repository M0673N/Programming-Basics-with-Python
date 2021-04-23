month = input()
nights = int(input())

if month == "May" or month == "October":
    studio = 50
    apt = 65
    if 14 > nights > 7:
        studio *= 0.95
    elif nights > 14:
        studio *= 0.7
elif month == "June" or month == "September":
    studio = 75.2
    apt = 68.7
    if nights > 14:
        studio *= 0.8
elif month == "July" or month == "August":
    studio = 76
    apt = 77

if nights > 14:
    apt *= 0.90

price_studio = studio * nights
price_apt = apt * nights

print(f"Apartment: {price_apt:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")
