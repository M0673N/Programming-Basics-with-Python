clients = int(input())
total_spent = 0
for i in range(clients):
    total_spent_client = 0
    total_stuff_per_client = 0
    while True:
        choice = input()
        if choice == "Finish":
            break
        if choice == "basket":
            total_spent_client += 1.5
            total_stuff_per_client += 1
        elif choice == "wreath":
            total_spent_client += 3.8
            total_stuff_per_client += 1
        else:
            total_spent_client += 7
            total_stuff_per_client += 1
    if total_stuff_per_client % 2 == 0:
        total_spent_client *= 0.8
    print(f"You purchased {total_stuff_per_client} items for {total_spent_client:.2f} leva.")
    total_spent += total_spent_client
else:
    print(f"Average bill per client is: {total_spent / clients:.2f} leva.")
