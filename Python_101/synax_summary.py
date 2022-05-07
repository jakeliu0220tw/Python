import os

def main():
    print("entry main()")
    print("this is main(), hello world")

    a = 5
    b = 10
    mysum = sum(a, b)
    print("sum of {0} and {1} is ... {2}".format(a, b, mysum))

    print('='*100)
    curr = os.getcwd()
    print("current directory is " + curr)

    # list
    foods = ["apple", "banana", "cherry"]
    # for loop
    for i in foods:
        print("I would like to eat {0}".format(i))

    # range
    print("count to 10")
    for i in range(10):
        print("i = {0}".format(i))


def sum(param1, param2):
    print("entry sum(), param1 = {0}, param2 = {1}".format(param1, param2))

    result = param1 + param2

    if result > 20:
        print('foo')
    elif result > 0 and result < 20:
        print('boo')
    else:
        print('moo')
    
    return result

if __name__ == "__main__":
    main()
