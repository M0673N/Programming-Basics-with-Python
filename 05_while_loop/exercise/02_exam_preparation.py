bad_grades = int(input())
name = input()
grade = int(input())
total_grade = 0
number_of_tests = 0
bad_grades_counter = 0
while name != "Enough":
    problem = name
    total_grade += grade
    number_of_tests += 1
    if grade <= 4:
        bad_grades_counter += 1
    if bad_grades_counter == bad_grades:
        print(f"You need a break, {bad_grades} poor grades.")
        break
    name = input()
    if name == "Enough":
        print(f"Average score: {(total_grade / number_of_tests):.2f}")
        print(f"Number of problems: {number_of_tests}")
        print(f"Last problem: {problem}")
        break
    grade = int(input())
