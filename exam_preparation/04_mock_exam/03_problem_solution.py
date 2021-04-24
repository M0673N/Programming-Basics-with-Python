country = input()
item = input()
points = 0
if country == "Bulgaria":
    if item == "ribbon":
        points = 19
    elif item == "hoop":
        points = 19.3
    elif item == "rope":
        points = 18.9
elif country == "Russia":
    if item == "ribbon":
        points = 18.5
    elif item == "hoop":
        points = 19.1
    elif item == "rope":
        points = 18.6
elif country == "Italy":
    if item == "ribbon":
        points = 18.7
    elif item == "hoop":
        points = 18.8
    elif item == "rope":
        points = 18.85
print(f"The team of {country} get {points:.3f} on {item}.")
print(f"{abs(points / 20 * 100 - 100):.2f}%")
