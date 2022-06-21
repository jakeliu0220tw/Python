# fromkeys()
seq1 = ['name', 'city']
my_dict1 = dict.fromkeys(seq1)
print(my_dict1)

seq2 = 'name', 'city'
my_dict2 = dict.fromkeys(seq2, 'unknown')
print(my_dict2)