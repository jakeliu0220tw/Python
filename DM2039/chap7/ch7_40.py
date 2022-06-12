buyers = [['jake', 20000], ['jean', 2000], ['william', 20000], ['anita', 2000],
          ['ziv', 2000], ['bob', 2000], ['cindy', 20000], ['dylan', 2000]]
vips = []
golds = []

print(buyers)
while(buyers):
    buyer = buyers.pop()
    if buyer[1] > 10000:
        vips.append(buyer)
    else:
        golds.append(buyer)
print(f'vips = {vips}')
print(f'golds = {golds}')