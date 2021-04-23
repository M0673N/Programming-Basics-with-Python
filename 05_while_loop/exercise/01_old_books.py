book = input()
command = input()
counter = 0
while command != "No More Books" and command != book:
    counter += 1
    command = input()
if command == "No More Books":
    print("The book you search is not here!")
    print(f"You checked {counter} books.")
elif command == book:
    print(f"You checked {counter} books and found it.")
