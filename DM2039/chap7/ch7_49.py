# use while loop to get answer

chicken = 0
legs = 100
active = True
while active:
    rabbits = 35 - chicken
    if (chicken * 2 + rabbits * 4) == legs:
        print(f"chicken => {chicken}, rabbits => {rabbits}")
    chicken += 1
    if chicken > 35:
        break