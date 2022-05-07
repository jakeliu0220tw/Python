#list => []
x = [1, 2, 3, 4, 5]
#index
print(x)
print(x[0])
print(x[-1])
#slicing
print(x[1:3])

#tuple, can't be modified => ()
x1 = (1,2,3,4,5)
print(x1)
# error
# x1[0] = 0
x2 = list("12345")
# x2 is the same with x2 = ['1','2','3','4','5']
print(x2)

#dict => {}
y = {'a': 1, 'b':2, 'c':3}
print(type(y))
print(y)
print(y.keys())
print(y.values())
print(y.items())

#set => {}, very similar with dict, but elements are all unique
# u is same with u = {'a', 'b', 'c', 'd'}
u = set("aabbccdd")
print(u)
v = set("cdef")
print(v)
print(u&v)
print(u|v)
print(u-v)