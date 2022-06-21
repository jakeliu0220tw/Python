# items(), keys(), values()
my_dict = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e'}
for k in my_dict.keys():
    print(f'key in my_dict => {k}')
for v in my_dict.values():
    print(f"value in my_dict => {v}")
for item in my_dict.items():
    print(f'item in my_dict => {item}')
for k, v in my_dict.items():
    print(f'{k} => {v}')