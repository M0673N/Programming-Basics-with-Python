name = input()
counter = 1
score = 0
exclusion_counter = 0
while counter <= 12:
    grade = float(input())
    if grade < 4:
        exclusion_counter += 1
        if exclusion_counter == 2:
            print(f"{name} has been excluded at {counter} grade")
            break
        continue
    score += grade
    counter += 1
if counter == 13 and exclusion_counter < 2:
    final_score = score / (counter - 1)
    print(f"{name} graduated. Average grade: {final_score:.2f}")
