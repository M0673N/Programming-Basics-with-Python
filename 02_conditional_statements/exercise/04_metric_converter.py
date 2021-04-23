number = float(input())
convert_from = input()
convert_to = input()

if convert_from == "m" and convert_to == "cm":
    print(f"{(number * 100):.3f}")
if convert_from == "m" and convert_to == "mm":
    print(f"{(number * 1000):.3f}")

if convert_from == "cm" and convert_to == "m":
    print(f"{(number / 100):.3f}")
if convert_from == "cm" and convert_to == "mm":
    print(f"{(number * 10):.3f}")

if convert_from == "mm" and convert_to == "cm":
    print(f"{(number / 10):.3f}")
if convert_from == "mm" and convert_to == "m":
    print(f"{(number / 1000):.3f}")
