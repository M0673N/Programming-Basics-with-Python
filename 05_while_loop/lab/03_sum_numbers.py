sum_max = int(input())
num = int(input())
current_sum = num
while current_sum < sum_max:
    num = int(input())
    current_sum += num
print(current_sum)
