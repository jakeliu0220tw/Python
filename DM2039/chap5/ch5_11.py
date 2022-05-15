# demo of way to use if
height = eval(input("please input your height(cm): "))
weight = eval(input("please input your weight(kg): "))
if bmi := weight / (height / 100)**2 >= 28:
    print("you are fat!")
else:
    print("you are fit.")