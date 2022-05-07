# list
a = [1, 2, 3, 4, 5]
for i in a:
    print("i = ", i)

# tuple
print("=" * 100)
b = (1, 2, 3, 4, 5)
for i in b:
    print("i = {0}".format(i))

# set
print("=" * 100)
c = {1, 2, 3, 4, 5}
for i in c:
    print("i = {0}".format(i))

# dict
print("=" * 100)
d = {'apple':'10', 'banana':'20', 'cherry':'30'}
for i in d:
    print("(key,value) => ({0}, {1})".format(i, d[i]))

# while loop
count = 0
while count < 10:
    print("count =", count)
    count += 1

# continue & break
print('=' * 100)
for i in range(1,10):
    if i % 5 == 0:
        continue
    if i % 8 == 0:
        break
    print(i)

print('=' * 100)
c = 0
while c < 10:
    c += 1
    if c % 5 == 0:
        continue
    if c % 8 == 0:
        break
    print(c)
