print(bool(""))
print(bool([]))

# list
a = list("this is a list")
print(a)
if bool(a):
    print("a is a list")
else:
    print("a is an empty list")

# string fillup
s = "this is {}\'s book"
print(s.format("bob"))
print(s.format("jake"))

s1 = "this is {who}\'s book"
print(s1.format(who = "Edgar"))
print(s1.format(who = "Harvey"))

s2 = "{0}, {1}, {2}"
print(s2.format("qqq", "uuu", "vvv"))

# string method
ss = "i am jake"
print(ss.capitalize())
print(ss.upper())

# none
d = None
if d:
    print("d exist")
else:
    print("d is none")


# int & float
a = 100
b = 20
print(a/b)
print(type(a/b))
print(a//b)
print(type(a//b))

# range
print(range(10))
for i in range(10):
    print(i)
