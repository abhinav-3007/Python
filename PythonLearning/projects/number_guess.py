import tkinter as tk
import random


def start():
    global exp
    global lives
    global chance
    global num
    global replay
    global entry
    global button
    chance = 6
    exp.set("")
    lives.set("Chances: " + str(chance))
    num = random.randint(1, 100)
    replay.config(state="disabled")
    entry.config(state="normal")
    entry.delete(0, 'end')
    button.config(state="normal")
    last_guess.set("")



def enter():
    global num
    global entry
    global button
    global chance
    global lives
    global game
    global played
    global w
    global wins
    global last_guess
    exp.set("")
    disp.config(fg="red")
    try:
        guess = int(entry.get().strip())
        expression = ""
        chance -= 1
        if guess == num:
            expression = "Correct Answer!!"
            disp.config(fg="Green")
            entry.config(state="disabled")
            button.config(state="disabled")
            replay.config(state="active")
            game+=1
            w+=1
        elif chance==0:
            expression=f"You Lost:(\nCorrect Answer: {num}"
            entry.config(state="disabled")
            button.config(state="disabled")
            replay.config(state="active")
            game+=1
        elif abs(guess - num) <= 2:
            expression = "Very Close!"
        elif abs(guess - num) <= 5:
            expression = "Close!"

        if guess < num and chance!=0:
            expression += "\nToo Low!"
        elif guess > num and chance!=0:
            expression += "\nToo High!"
        exp.set(expression)
        last_guess.set("Last Guess: " + str(guess))

    except ValueError as ve:
        exp.set("Please enter a valid value")
        print("ValueError:",ve)
    except Exception as e:
        print("Exception:",e)
        exp.set("Error")
    finally:
        entry.delete(0, "end")
        lives.set("Lives: "+str(chance))
        played.set("Games Finished: " + str(game))
        wins.set("Games Won: " + str(w))


root = tk.Tk()
root.title("Guess the Number")
root.resizable(0, 0)

exp = tk.StringVar()
last_guess = tk.StringVar()
lives = tk.StringVar()

num = 0

chance = 6

game = 0
played = tk.StringVar()
played.set("Games Finished: "+str(game))

w = 0
wins = tk.StringVar()
wins.set("Games Won: "+str(w))

description = tk.Label(root, text="This game is about guessing numbers between 1 and 100.\n"
                                  "To play, enter your guess in the box given below and enter it.\n"
                                  "The game will alert you about whether your guess is lower or higher than the number."
                                  "\nYou get 6 lives. When these are lost or you guess the number, the game ends.",
                       fg="blue", font=["Times New Roman", 15])
description.grid(row=1, columnspan=7)

lifedisp = tk.Label(root, textvariable=lives, fg="Dark Red", font=["Times New Roman", 15])
lifedisp.grid(row=2, columnspan=7)

last = tk.Label(root, textvariable=last_guess, fg="Dark Green", font=["Times New Roman", 15])
last.grid(row = 3, columnspan = 7)

label= tk.Label(root, text="Your Guess:", font=["Times New Roman", 15])
label.grid(row=4, column=2)

entry = tk.Entry(root, font=["Times New Roman", 15])
entry.grid(row=4, column=3)

button=tk.Button(root,text="Enter", command=enter, font=["Times New Roman", 15])
button.grid(row=4, column=4)

disp = tk.Label(root, textvariable = exp, font=["Times New Roman", 15])
disp.grid(row=5, columnspan=7)

play = tk.Label(root, textvariable=played, font=["Times New Roman", 15], fg="Lime Green")
play.grid(row=6, columnspan = 7)

victory = tk.Label(root, textvariable=wins, font=["Times New Roman", 15], fg = "Lime Green")
victory.grid(row=7, columnspan=7)

replay = tk.Button(root, text="Play Again", state="disabled",font=["Times New Roman", 15] , command=start)
replay.grid(row=8, columnspan=7)

start()

root.mainloop()
