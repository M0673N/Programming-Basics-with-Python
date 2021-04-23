width = int(input())
length = int(input())
height = int(input())
crates = input()
space = width * length * height
while crates != "Done":
    crates_1 = int(crates)
    space -= crates_1
    if space < 0:
        print(f"No more free space! You need {abs(space)} Cubic meters more.")
        break
    crates = input()
if space >= 0:
    print(f"{space} Cubic meters left.")
