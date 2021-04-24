total_eggs = int(input())
red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0
max_eggs = 0
for i in range(total_eggs):
    egg = input()
    if egg == "red":
        red_eggs += 1
    elif egg == "orange":
        orange_eggs += 1
    elif egg == "blue":
        blue_eggs += 1
    elif egg == "green":
        green_eggs += 1
print(f"Red eggs: {red_eggs}")
print(f"Orange eggs: {orange_eggs}")
print(f"Blue eggs: {blue_eggs}")
print(f"Green eggs: {green_eggs}")
if red_eggs > orange_eggs and red_eggs > blue_eggs and red_eggs > green_eggs:
    print(f"Max eggs: {red_eggs} -> red")
elif orange_eggs > red_eggs and orange_eggs > blue_eggs and orange_eggs > green_eggs:
    print(f"Max eggs: {orange_eggs} -> orange")
elif blue_eggs > red_eggs and blue_eggs > orange_eggs and blue_eggs > green_eggs:
    print(f"Max eggs: {blue_eggs} -> blue")
else:
    print(f"Max eggs: {green_eggs} -> green")
