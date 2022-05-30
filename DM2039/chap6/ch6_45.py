# string is a list of char
str = 'python'

print(str)
for s in str:
    print(s)

print(str[0:3])
print(str[0:-1])
print(str[:])

ch1, ch2, *ch3 = str
print(f'ch1 = {ch1}')
print(f'ch2 = {ch2}')
print(f'ch3 = {ch3}')

my_list = list('aaBBccDD')
print(f'my_list = {my_list}')
