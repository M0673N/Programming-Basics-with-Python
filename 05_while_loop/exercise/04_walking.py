steps = 0
while steps < 10000:
    going_out = input()
    if going_out == "Going home":
        going_home_steps = int(input())
        steps += going_home_steps
        if steps < 10000:
            print(f"{10000 - steps} more steps to reach goal.")
        break
    going_out_steps = int(going_out)
    steps += going_out_steps

if steps >= 10000:
    print(f"Goal reached! Good job!\n"
          f"{steps - 10000} steps over the goal!")
