# remove elements in list
list_1 = [1, 2, 3, 4, 5, 6, 7, 8]
list_2 = [2, 3, 4, 55, 66, 77, 88]
print(list_1)
print(list_2)

# remove elements in list_2 if they are parts of list_1
for e in list_2[:]:
    if e in list_1:
        list_2.remove(e)
print(list_2)