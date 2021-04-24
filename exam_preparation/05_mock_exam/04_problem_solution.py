p1 = int(input())
p2 = int(input())
command = input()
while command != "End of battle":
    if command == "one":
        p2 -= 1
    else:
        p1 -= 1
    if p1 == 0:
        print(f"Player one is out of eggs. Player two has {p2} eggs left.")
        break
    if p2 == 0:
        print(f"Player two is out of eggs. Player one has {p1} eggs left.")
        break
    command = input()
else:
    print(f"Player one has {p1} eggs left.")
    print(f"Player two has {p2} eggs left.")
