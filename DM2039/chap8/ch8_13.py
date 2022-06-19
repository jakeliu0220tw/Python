# use enumerate() in list
drinks = ["water", "juice", "coffee"]
for drink in drinks:
    print(drink)

enumerate_drinks = enumerate(drinks)
for drink in enumerate_drinks:
    print(drink)

# use enumerate() in tuple
colors = ('red', 'yellow', 'green')
for color in colors:
    print(color)
for color in enumerate(colors):
    print(color)
for count, color in enumerate(colors):
    print(f"count={count}, color={color}")