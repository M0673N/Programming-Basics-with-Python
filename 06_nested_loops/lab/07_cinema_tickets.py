movie = input()
students = 0
standards = 0
kids = 0
while movie != "Finish":
    theatre_size = int(input())
    seats = input()
    count = 0
    while theatre_size > count and seats != "End":
        count += 1
        if seats == "student":
            students += 1
        elif seats == "standard":
            standards += 1
        else:
            kids += 1
        if count == theatre_size:
            break
        seats = input()
    percent = (count / theatre_size) * 100
    print(f"{movie} - {percent:.2f}% full.")
    movie = input()
total_tickets = students + standards + kids
print(f"Total tickets: {total_tickets}\n"
      f"{((students / total_tickets) * 100):.2f}% student tickets.\n"
      f"{((standards / total_tickets) * 100):.2f}% standard tickets.\n"
      f"{((kids / total_tickets) * 100):.2f}% kids tickets.")
