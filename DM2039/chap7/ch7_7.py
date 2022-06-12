# demo of endwith(), startwith()
files = ['main.py', 'readme.txt', 'test.py', 'unknown']
py_files = []
names = ['jake', 'eva', 'john', 'cindy', 'jazz']
names_begin_with_j = []

for file in files:
    if file.endswith('py'):
        py_files.append(file)
print(py_files)

for name in names:
    if name.startswith('j'): names_begin_with_j.append(name)
print(names_begin_with_j)