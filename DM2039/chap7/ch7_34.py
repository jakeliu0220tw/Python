# demo of while loop => calculate tution

tution = 50000
count = 1
while tution < 60000:
    tution = tution * (1.05)
    count += 1
print(f"{count} years later, the tution will exceed 60000")