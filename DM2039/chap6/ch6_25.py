# demo of del & pop & remove
cars = ['Nissan', 'Bmw', 'Ford', 'Honda', 'Toyota']
print(f"cars = {cars}")

del cars[len(cars)-1]
print(f"cars = {cars}")

# pop up the last element of list
poped_car = cars.pop()
print(f"poped_car = {poped_car}")
print(f"cars = {cars}")

# remove elements with special value
cars.remove('Ford')
print(f"cars = {cars}")
