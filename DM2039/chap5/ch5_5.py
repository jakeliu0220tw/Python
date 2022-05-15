# demo of simple if/else statement

x, y = eval(input("please input 2 num: "))
max_ = x if x > y else y
print(f"max num is {max_}")
min_ = x if x < y else x
print(f"min num is {min_}")