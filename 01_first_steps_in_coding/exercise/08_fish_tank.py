length = int(input())
width = int(input())
height = int(input())
filled_space = float(input())
cubic_centimeters = length * width * height - (length * width * height) * filled_space / 100
print(cubic_centimeters / 1000)
