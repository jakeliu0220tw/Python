# print out data to file
f1 = open("test1.txt", mode="w")
print("content for test1.txt", file=f1)
f1.close()
# append data to file
f2 = open("test2.txt", mode="a")
print("content for test2.txt", file=f2)
f2.close()