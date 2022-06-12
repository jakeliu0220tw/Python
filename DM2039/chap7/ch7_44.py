# demo of emuerate object
scores = [21, 29, 18, 33, 12, 17, 26, 28, 15, 19]

# traditional way
count = 0
for s in scores:
    count += 1
    if s > 20:
        print(f"num: {count}, the scores > 20 => {s}")

# enumerate way
for idx, score in enumerate(scores):
    if score > 20:
        print(f"num: {idx+1}, the scores > 20 => {score}")
