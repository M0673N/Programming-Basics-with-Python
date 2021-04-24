from math import floor

name = input()
seasons = int(input())
episodes = int(input())
minutes = float(input())
print(f"Total time needed to watch the {name} series is {floor(seasons * (episodes * minutes * 1.2 + 10))} minutes.")
