target = int(input())
total_jumps = 0
flag1 = False
for height in range(target - 30, target + 1, 5):
    for attempt in range(1, 4):
        jump = int(input())
        if jump > height:
            total_jumps += attempt
            break
    else:
        total_jumps += attempt
        print(f"Tihomir failed at {height}cm after {total_jumps} jumps.")
        flag1 = True
        break
    if flag1:
        break
else:
    print(f"Tihomir succeeded, he jumped over {height}cm after {total_jumps} jumps.")
