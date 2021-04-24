days = int(input())
total = 0
wins = 0
losses = 0
for day in range(1, days + 1):
    total_day = 0
    wins_day = 0
    losses_day = 0
    game = input()
    while game != "Finish":
        result = input()
        if result == "win":
            total_day += 20
            wins_day += 1
        else:
            losses_day += 1
        game = input()
    wins += wins_day
    losses += losses_day
    if wins_day > losses_day:
        total += total_day * 1.1
    else:
        total += total_day
if wins > losses:
    total *= 1.2
    print(f"You won the tournament! Total raised money: {total:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total:.2f}")
