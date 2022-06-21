# get() & setdefault()
list1 = ['apple', 'banana', 'orange']
list2 = [15, 20, 25]
zip_data = zip(list1, list2)
fruits = dict(zip_data)
print(fruits)

# get()
apple_price = fruits.get('apple', None)
print(apple_price)
cherry_price = fruits.get('cherry')
print(cherry_price)
# setdefault()
orange_price = fruits.setdefault('orange', 35)
print(orange_price)
melon_price = fruits.setdefault('melon', 35)
print(melon_price)
