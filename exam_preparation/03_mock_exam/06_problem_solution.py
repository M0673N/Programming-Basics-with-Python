name = input()
films = 0
highest = 0
highest_name = ""
while name != "STOP":
    points = 0
    for char in name:
        points += ord(char)
        if 65 <= ord(char) <= 90:
            points -= len(name)
        elif 97 <= ord(char) <= 122:
            points -= len(name) * 2
    if highest < points:
        highest = points
        highest_name = name
    films += 1
    if films == 7:
        break
    name = input()
if films == 7:
    print("The limit is reached.")
print(f"The best movie for you is {highest_name} with {highest} ASCII sum.")
