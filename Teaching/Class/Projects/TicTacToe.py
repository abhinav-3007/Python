# printing board
def board():
    print("Player 1: |||; Player 2: ---")
    print("     |     |     ")
    print(f" {r[0]} | {r[1]} | {r[2]} ")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f" {r[3]} | {r[4]} | {r[5]} ")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f" {r[6]} | {r[7]} | {r[8]} ")
    print("     |     |     ")


# Checking who won
def winner():
    global running
    running = False
    if turn == 2:
        print("Player 1 Won!")
    else:
        print("Player 2 Won!")


r = [' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ', ' 9 ']
count = 0

print("Tic-Tac-Toe\nby Abhinav Goyal")

turn = 1
running = True
while running:
    board()
    print(f'Player {turn}\'s turn')
    choice = int(input('Enter position\t')) - 1

    # Checking if input is valid
    if choice <= 8 and r[choice].strip().isnumeric():
        # Putting symbols on board
        if turn == 1:
            r[choice] = '|||'
            turn = 2
        else:
            r[choice] = '---'
            turn = 1
        count += 1


    if r[0] == r[3] == r[6]:
        board()
        winner()
    elif r[1] == r[4] == r[7]:
        board()
        winner()
    elif r[2] == r[5] == r[8]:
        board()
        winner()
    elif r[0] == r[1] == r[2]:
        board()
        winner()
    elif r[3] == r[4] == r[5]:
        board()
        winner()
    elif r[6] == r[7] == r[8]:
        board()
        winner()
    elif r[0] == r[4] == r[8]:
        board()
        winner()
    elif r[2] == r[4] == r[6]:
        board()
        winner()
    elif count == 9:
        board()
        print('Draw :/')
        running = False
