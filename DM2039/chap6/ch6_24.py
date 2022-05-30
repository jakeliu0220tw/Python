# demo of append / insert
cars = []
cars.append('Bmw')
print(f"cars = {cars}")

cars.append('Ford')
cars.append('Honda')
print(f"cars = {cars}")

cars.insert(0, "Nissan")
print(f"cars = {cars}")
cars.insert(len(cars), "Toyota")
print(f"cars = {cars}")