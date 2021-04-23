from math import floor

record = float(input())
distance = float(input())
secs_per_meter = float(input())

slowdown = floor(distance / 15) * 12.5
time = secs_per_meter * distance
total_time = time + slowdown

if total_time < record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {(total_time - record):.2f} seconds slower.")
