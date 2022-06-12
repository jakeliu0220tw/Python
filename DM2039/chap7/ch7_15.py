# demo of list generator
# generate a list from 1 to 20

# method1
list_1 = []
for n in range(21):
    list_1.append(n)
print(list_1)

# mehtod2
list_2 = list(range(21))
print(list_2)

# method3
list_3 = [n for n in range(21)]
print(list_3)