from random import randint

rock = '👊'
paper = '✋'
scissor = '✌'

rounds = int(input('Enter no. of rounds:\n'))

for i in range(rounds):
    choice = int(input('Enter your choice:\n'
                       f'1[{rock}]\t2[{paper}]\t3[{scissor}]\n'))
    if choice > 3 or choice < 1:
        print("ur a cheater and ur dum. Stop. loser.")
        break

    comp = randint(1, 3)
    print(comp)
