from math import floor
year = input()
holidays = int(input())
travel_holidays = int(input())

home_weekends = 48 - travel_holidays
sofia_weekends = home_weekends * 3 / 4
free_holidays = holidays * 2 / 3
playtime = sofia_weekends + travel_holidays + free_holidays

if year == "leap":
    playtime *= 1.15

print(floor(playtime))
