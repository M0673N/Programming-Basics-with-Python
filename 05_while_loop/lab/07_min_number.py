from sys import maxsize

number = input()
smallest = maxsize
while number != "Stop":
    if int(number) < smallest:
        smallest = int(number)
    number = input()
print(smallest)
