fruits = {'apple':15, 'banana':20, 'melon':40}
print(fruits)

key = input('please choose the fruit you want to buy: ')
if key in fruits:
    print(f'price of {key} is {fruits[key]}')
else:
    print(f'sorry, the {key} not exists')