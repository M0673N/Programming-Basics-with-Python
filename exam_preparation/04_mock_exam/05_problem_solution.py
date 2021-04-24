from math import floor

championships = int(input())
starting_points = int(input())
earned_points = 0
counter = 0
for championship in range(championships):
    result = input()
    if result == "W":
        starting_points += 2000
        earned_points += 2000
        counter += 1
    elif result == "F":
        starting_points += 1200
        earned_points += 1200
    else:
        starting_points += 720
        earned_points += 720
print(f"Final points: {starting_points}")
print(f"Average points: {floor(earned_points / (championship + 1))}")
print(f"{counter / (championship + 1) * 100:.2f}%")
