from sys import maxsize

number = input()
biggest = -maxsize
while number != "Stop":
    if int(number) > biggest:
        biggest = int(number)
    number = input()
print(biggest)
