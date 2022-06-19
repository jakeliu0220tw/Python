# tuple & list exchange
keys = 1, 2, 3
print(type(keys))
print(f"keys = {keys}")

key_list = list(keys)
print(f"key_list = {key_list}")

another_key_list = [4, 5, 6]
key_tuple = tuple(another_key_list)
print(type(key_tuple))
print(f"key_tuple = {key_tuple}")