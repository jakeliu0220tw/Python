# demo of while loop
mylist = [1, 2, 3, 4, 5, 1, 1, 2, 1, 1]
print(mylist)

x = 1
while x in mylist:
    mylist.remove(x)
print(mylist)