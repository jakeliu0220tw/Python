# demo of reverse() / sort() / sorted()
my_list = [1, 2, 3, 4, 5]
new_list = [5, 4, 3, 2, 1]
print(f'my_list = {my_list}')

# reverse
my_list.reverse()
print(f'my_list = {my_list}')

# return reversed list
print(f'my_list_reverse = {my_list[::-1]}')

# sort
my_list.sort()
print(f'mylist after sort() = {my_list}')

# return sorted list
print(f'new_list after sorted() = {sorted(new_list)}')

