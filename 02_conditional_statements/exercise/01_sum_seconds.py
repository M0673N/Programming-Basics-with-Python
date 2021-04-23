competitor_1 = int(input())
competitor_2 = int(input())
competitor_3 = int(input())

total = competitor_1 + competitor_2 + competitor_3

minutes = total // 60
seconds = total % 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")
