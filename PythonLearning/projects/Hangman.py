import tkinter as tk
import random
import csv

blanked = ''
li = []
guessed_li = []


def blanks():
    global movie
    global blanked
    global li
    li = [False for x in range(len(movie))]
    blanked = movie

    for i in range(len(li)):
        if movie[i] != " ":
            blanked = blanked.replace(blanked[i],'_')
    var.set(blanked)


def enter():
    global entry1
    global movie
    global blanked
    global lives
    global var
    global guessed_li
    guess = entry1.get().upper()
    if guess != ' ' and guess not in guessed_li and guess.isalpha() and len(guess)==1:
        guessed_li.append(guess)
        try:
            if movie.count(guess) != blanked.count(guess):
                ind = movie.index(guess)
            while movie.count(guess) != blanked.count(guess):
                blanked = blanked[:ind] + guess + blanked[ind+1:]
                var.set(blanked)
                ind = movie.index(guess, ind + 1)
            else:
                lives-=1
                lives_str.set("Lives: " + str(lives))
        except ValueError as ve:
            print("Value error:",ve)
        except Exception as e:
            print("Exception",e)
    entry1.delete(0, 'end')
    guessed.set("Guessed Values:    " + ", ".join(sorted(guessed_li)))
    if lives<=0:
        win.set("You Lost!! :(")
        win_text.config(fg="Red")
        entry1.config(state="disabled")
    elif blanked == movie:
        win.set("You Win!! :)")
        win_text.config(fg="Green")
        entry1.config(state="disabled")


root = tk.Tk()
root.title("Hangman")
root.resizable(0,0)

lives = 10
lives_str = tk.StringVar()
lives_str.set("Lives: " + str(lives))

win = tk.StringVar()

guessed = tk.StringVar()

with open('movies.csv') as f:
    reader = csv.reader(f)
    file = list(reader)
movie_li = []
movie_li.extend(file[0])
movie = " ".join(list(movie_li[random.randint(0,len(movie_li)-1)])).strip()

rules = tk.Label(root, text = "HOW TO PLAY:\n 1. Your goal is to guess the name of the movie thought of by the system.\n"
                              " 2. You get 10 lives and each time you get a letter wrong, you lose a life.\n"
                              " 3. Each time you guess a letter correctly, the blanks which contain that letter will get filled up.\n"
                              " 4. If you manage to guess the movie correcty, you win, else, you lose.", fg = "Orange", font = ("Times New Roman", 15))
rules.grid(row = 1, columnspan= 4)

lives_text = tk.Label(root, textvariable=lives_str, fg="Gold", font=("Times New Roman", 15))

lives_text.grid(row=2, columnspan=4)

var = tk.StringVar()

blanks()

var.set(blanked)

movie_label = tk.Label(root, textvariable = var, fg = "Blue", font = ("Times New Roman", 15))
movie_label.grid(row = 3, columnspan = 4)

letter = tk.Label(root, text = "Enter your guess(Single Letter): ", fg = "Dark Green", font = ("Times New Roman", 15))
entry1 = tk.Entry(root, fg = "Dark Green", font = ("Times New Roman", 15))
button1 = tk.Button(root, text = "Enter Guess", fg = "Dark Green", font = ("Times New Roman", 15), command = enter)
letter.grid(row = 4, column = 1)
entry1.grid(row = 4, column = 2)
button1.grid(row = 4, column = 3)

guessed_label = tk.Label(root, textvariable=guessed, fg="Navy" , font=("Times New Roman", 15))
guessed_label.grid(row = 5, columnspan= 4)

win_text = tk.Label(root, textvariable=win, font = ("Times New Roman", 15))
win_text.grid(row = 6, columnspan = 4)

root.mainloop()
