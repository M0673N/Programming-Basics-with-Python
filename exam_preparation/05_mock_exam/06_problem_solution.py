cozonac = int(input())
n1 = 0
current_leader = ""
current_leader_score = 0
for i in range(cozonac):
    name = input()
    grade = input()
    total_grade = 0
    while grade != "Stop":
        total_grade += int(grade)
        grade = input()
    print(f"{name} has {total_grade} points.")
    if total_grade > n1:
        n1 = total_grade
        current_leader = name
        current_leader_score = total_grade
        print(f"{current_leader} is the new number 1!")
print(f"{current_leader} won competition with {current_leader_score} points!")
