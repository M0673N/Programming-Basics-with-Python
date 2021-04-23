number = input()
non_prime_sum = 0
prime_sum = 0
while number != "stop":
    if int(number) > 1:
        for i in range(2, int(number)):
            if int(number) % i == 0:
                prime_sum += int(number)
                break
        else:
            non_prime_sum += int(number)
    elif int(number) < 0:
        print("Number is negative.")
    number = input()
print(f"Sum of all prime numbers is: {non_prime_sum}")
print(f"Sum of all non prime numbers is: {prime_sum}")
