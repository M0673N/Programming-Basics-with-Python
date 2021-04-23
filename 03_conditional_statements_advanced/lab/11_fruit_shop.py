fruit = input()
day = input()
amount = float(input())

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    banana = 2.5
    apple = 1.2
    orange = 0.85
    grapefruit = 1.45
    kiwi = 2.7
    pineapple = 5.5
    grapes = 3.85
    if fruit == "banana":
        price = banana * amount
    elif fruit == "apple":
        price = apple * amount
    elif fruit == "orange":
        price = orange * amount
    elif fruit == "grapefruit":
        price = grapefruit * amount
    elif fruit == "kiwi":
        price = kiwi * amount
    elif fruit == "pineapple":
        price = pineapple * amount
    elif fruit == "grapes":
        price = grapes * amount
    else:
        price = 0

elif day == "Saturday" or day == "Sunday":
    banana = 2.7
    apple = 1.25
    orange = 0.9
    grapefruit = 1.6
    kiwi = 3
    pineapple = 5.6
    grapes = 4.2
    if fruit == "banana":
        price = banana * amount
    elif fruit == "apple":
        price = apple * amount
    elif fruit == "orange":
        price = orange * amount
    elif fruit == "grapefruit":
        price = grapefruit * amount
    elif fruit == "kiwi":
        price = kiwi * amount
    elif fruit == "pineapple":
        price = pineapple * amount
    elif fruit == "grapes":
        price = grapes * amount
    else:
        price = 0

else:
    price = 0

if price == 0:
    print("error")
else:
    print(f"{price:.2f}")
