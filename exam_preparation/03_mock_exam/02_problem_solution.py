from math import ceil

name = input()
episode_length = int(input())
break_length = int(input())
if episode_length + break_length / 8 + break_length / 4 <= break_length:
    print(
        f"You have enough time to watch {name} and left \
        with {ceil(break_length - (episode_length + break_length / 8 + break_length / 4))} minutes free time.")
else:
    print(
        f"You don't have enough time to watch {name}, you \
        need {ceil((episode_length + break_length / 8 + break_length / 4) - break_length)} more minutes.")
