age = float(input())
sx = input()

if sx == "m":
    if age >= 16:
        print("Mr.")
    else:
        print("Master")
elif sx == "f":
    if age >= 16:
        print("Ms.")
    else:
        print("Miss")
