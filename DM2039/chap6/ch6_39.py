# difference of append() & extend()
list_a = [1, 2, 3, 4]
list_b = [5, 6, 7, 8]
list_c = []
print(f'list_a = {list_a}')
print(f'list_b = {list_b}')

list_c.extend(list_a)
print(f'list_c = {list_c}')

list_c.append(list_b)
print(f"list_c = {list_c}")