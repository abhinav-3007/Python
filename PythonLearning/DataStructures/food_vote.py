vote = input('Enter votes: ').split()
vset = list(set(vote))
check = 0
tot = len(vote)
half = int(tot/2)
for i in vset:
    if vote.count(i) > int(tot/2):
        check = 1
        print("The winner of the vote is "+i)
        break
if check != 1:
    print("The kids will starve because they cannot decide on one food!")
