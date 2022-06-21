# demo of dict generator
# input_str = 'this is a simple sentence'
# try to print out each alphabet "counts" occur in my_str.
# 'a' => 1
# 's' => 4
# ' ' => 4

# method1
def CharCounter1(input_str):
    print(input_str)
    my_dict = {}
    for ch in input_str:
        count = my_dict.get(ch, None)
        if count == None:
            my_dict[ch] = 1
        else:
            my_dict[ch] = my_dict[ch] + 1
    # print(my_dict)
    for ch in sorted(my_dict.keys()):
        print(f'{ch} => {my_dict.get(ch)}')

# mehod2
def CharCounter2(input_str):
    print(input_str)
    my_dict = {ch:input_str.count(ch) for ch in input_str}
    # print(my_dict)
    for ch in sorted(my_dict.keys()):
        print(f'{ch} => {my_dict.get(ch)}')


if __name__ == '__main__':
    my_str = 'this is a simple sentence'
    CharCounter1(my_str)
    CharCounter2(my_str)
    CharCounter1('FACEBOOK')
    CharCounter2('APPLE')
    ...

