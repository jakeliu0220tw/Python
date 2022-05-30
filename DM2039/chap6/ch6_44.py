# demo of list[:] and copy
list = [1,2,3,4,5]
list_a = list[:]
list_b = list.copy()

print(f"list = {list}")
print(f'list_a = {list_a}')
print(f'list_b = {list_b}')

del list[0]
list_a.pop()
list_b.append(6)
print(f"list = {list}")
print(f'list_a = {list_a}')
print(f'list_b = {list_b}')
