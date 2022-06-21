# del one element from dict
mydict = {'a':'apple', 'b':'banana', 'c':'cherry'}
print(f'mydict = {mydict}')

# del() and pop()
del mydict['a']
print(f'mydict = {mydict}')
ret = mydict.pop('b', None)
print(f'ret = {ret}')
print(f'mydict = {mydict}')
ret = mydict.pop('f', None)
print(f'ret = {ret}')