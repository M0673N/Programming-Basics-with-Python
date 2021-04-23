n = int(input())
for num in range(1111, 10000):
    counter = 0
    text = str(num)
    for char_num in text:
        if int(char_num) != 0:
            if n % int(char_num) == 0:
                counter += 1
    if counter == 4:
        print(num, end=" ")
