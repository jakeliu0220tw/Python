# demo of range()

n = 20
for num in range(n):
    print('**' * num)

capital = 5000
rate = 0.05
for y in range(20):
    capital = capital * (1 + rate)
    print(f"the end of the {y} year, capital = {capital}")