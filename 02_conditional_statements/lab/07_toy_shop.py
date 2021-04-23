tour_price = float(input())
puzzles_count = int(input())
dolls_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

puzzle_price = 2.60
doll_price = 3
bear_price = 4.10
minion_price = 8.20
truck_price = 2

total_price = puzzle_price * puzzles_count + doll_price * dolls_count + bear_price * bears_count + minions_count \
              * minion_price + truck_price * trucks_count
if (puzzles_count + dolls_count + bears_count + minions_count + trucks_count) >= 50:
    total_price -= total_price * 0.25

total_price -= total_price * 0.10

if total_price >= tour_price:
    print(f"Yes! {total_price - tour_price:.2f} lv left.")
else:
    print(f"Not enough money! {tour_price - total_price:.2f} lv needed.")
