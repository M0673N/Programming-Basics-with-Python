n = int(input())
presentation_name = input()
total = 0
counter = 0
while presentation_name != "Finish":
    average = 0
    for i in range(n):
        grade = float(input())
        average += grade
        total += grade
    print(f"{presentation_name} - {(average / n):.2f}.")
    counter += 1
    presentation_name = input()
print(f"Student's final assessment is {(total / (n * counter)):.2f}.")
