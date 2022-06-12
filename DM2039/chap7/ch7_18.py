# demo of list generator

squares = [n**2 for n in range(11)]
print(squares)

# a pythagorean triple
x = [[a,b,c] for a in range(1,20) for b in range(a,20) for c in range(b,20) if (a**2 + b**2) == c**2]
print(x)

colors = ['red', 'green', 'blue']
shapes = ['circle', 'square', 'line']
y = [[c,s] for c in colors for s in shapes]
print(y)
for c,s in y:
    print(c, s)

# list generator with if statement
z = [n for n in range(1,21) if n%2 == 0]
print(z)
