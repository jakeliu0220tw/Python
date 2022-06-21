# sorted()
my_dict = {5:'e', 3:'c', 1:'a', 2:'b', 4:'d'}
print(my_dict)
for key in sorted(my_dict.keys()):
    print(f'key = {key}, value = {my_dict[key]}')