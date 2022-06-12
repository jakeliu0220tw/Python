scores = [11, 22, 33, 44, 55, 66, 77, 88, 99]
scores.sort(reverse=True)
print(scores)
count = 1
for s in scores:
    print(s)
    count += 1
    if count > 5: break
