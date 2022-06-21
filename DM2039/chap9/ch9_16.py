# merge two dict
dictA = {1:'toyota', 2:'ford', 3:'nissan'}
dictB = {4:'benz', 5:'farari'}
dictC = {**dictA, **dictB}

print(f'dictA = {dictA}')
print(f'dictB = {dictB}')
print(f'dictC = {dictC}')
