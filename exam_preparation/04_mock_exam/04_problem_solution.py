p1 = input()
p2 = input()
card1 = input()
p1_points = 0
p2_points = 0
while card1 != "End of game":
    card2 = int(input())
    if int(card1) > card2:
        p1_points += int(card1) - card2
    elif int(card1) < card2:
        p2_points += card2 - int(card1)
    else:
        print("Number wars!")
        card1 = int(input())
        card2 = int(input())
        if card1 > card2:
            print(f"{p1} is winner with {p1_points} points")
            break
        elif card1 < card2:
            print(f"{p2} is winner with {p2_points} points")
            break
    card1 = input()
else:
    print(f"{p1} has {p1_points} points")
    print(f"{p2} has {p2_points} points")
