start = int(input())
end = int(input())
magic = int(input())
counter = 0
flag = False
for num_1 in range(start, end + 1):
    for num_2 in range(start, end + 1):
        counter += 1
        if num_1 + num_2 == magic:
            print(f"Combination N:{counter} ({num_1} + {num_2} = {magic})")
            flag = True
            break
    if flag:
        break
if not flag:
    print(f"{counter} combinations - neither equals {magic}")
