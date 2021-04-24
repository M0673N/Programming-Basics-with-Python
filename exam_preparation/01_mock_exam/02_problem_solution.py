minutes = int(input())
walks = int(input())
calories = int(input())
usage = minutes * 5 * walks
if usage >= calories / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {usage}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {usage}.")
