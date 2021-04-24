flower_price = float(input())
kg_flower = float(input())
kg_sugar = float(input())
egg_cartons = int(input())
yeast = int(input())
sugar_price = flower_price * 0.75
egg_carton_price = flower_price * 1.1
yeast_price = sugar_price * 0.2
print(f"{flower_price * kg_flower + sugar_price * kg_sugar + egg_carton_price * egg_cartons + yeast * yeast_price:.2f}")
