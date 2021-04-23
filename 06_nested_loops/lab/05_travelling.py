destination = input()
while destination != "End":
    min_budget = float(input())
    total_saved = 0
    while total_saved < min_budget:
        total_saved += float(input())
    print(f"Going to {destination}!")
    destination = input()
