name = input()
password = input()
entered_pass = input()
while password != entered_pass:
    entered_pass = input()
print(f"Welcome {name}!")
