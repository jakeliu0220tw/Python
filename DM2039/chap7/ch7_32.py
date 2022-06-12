# demo of while loop => guess number game

answer = 30
guess = 0
active = True
while active:
    num = int(input("please enter a number between 0 and 100 : 99"))
    if num > answer:
        print("how about give a smaller number?")
    elif num < answer:
        print("how about give a larger number?")
    else:
        print("Wow! you are right!")
        active = False

