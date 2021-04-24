result_1 = input()
result_2 = input()
result_3 = input()
wins = 0
losses = 0
draws = 0
if int(result_1[0]) > int(result_1[2]):
    wins += 1
elif int(result_1[0]) == int(result_1[2]):
    draws += 1
else:
    losses += 1
if int(result_2[0]) > int(result_2[2]):
    wins += 1
elif int(result_2[0]) == int(result_2[2]):
    draws += 1
else:
    losses += 1
if int(result_3[0]) > int(result_3[2]):
    wins += 1
elif int(result_3[0]) == int(result_3[2]):
    draws += 1
else:
    losses += 1
print(f"Team won {wins} games.")
print(f"Team lost {losses} games.")
print(f"Drawn games: {draws}")
