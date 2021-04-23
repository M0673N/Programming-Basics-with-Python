start = int(input())
end = int(input())
for num in range(start, end + 1):
    left = int(str(num)[0]) + int(str(num)[2]) + int(str(num)[4])
    right = int(str(num)[1]) + int(str(num)[3]) + int(str(num)[5])
    if left == right:
        print(num, end=" ")
