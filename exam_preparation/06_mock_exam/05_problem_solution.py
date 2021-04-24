cozonacs = int(input())
sugar_max = 0
flour_max = 0
total_sugar = 0
total_flour = 0
for cozonac in range(cozonacs):
    sugar = int(input())
    flour = int(input())
    if sugar_max < sugar:
        sugar_max = sugar
    if flour_max < flour:
        flour_max = flour
    total_flour += flour
    total_sugar += sugar
else:
    sugar_packages = total_sugar // 950
    if total_sugar % 950 != 0:
        sugar_packages += 1
    flour_packages = total_flour // 750
    if total_sugar % 750 != 0:
        flour_packages += 1
    print(f"Sugar: {sugar_packages}\n"
          f"Flour: {flour_packages}\n"
          f"Max used flour is {flour_max} grams, max used sugar is {sugar_max} grams.")
