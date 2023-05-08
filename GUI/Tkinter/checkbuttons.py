import tkinter as tk


def clickorder():
    message = "Your order is "
    if var1.get() == 1 and var2.get() == 1:
        message += "Pizza and Burger"
    elif var1.get() == 1:
        message += "Pizza"
    elif var2.get() == 1:
        message += "Burger"
    else:
        message = "You have no order"
    popup = tk.Toplevel()
    label2 = tk.Label(popup, text=message)
    label2.pack()


root = tk.Tk()

label = tk.Label(root, text="What to eat?")
label.pack()
root.title("Menu")

var1 = tk.IntVar()
var2 = tk.IntVar()
check1 = tk.Checkbutton(root, text="Pizza", variable=var1, onvalue=1, offvalue=0)
check1.pack()

check2 = tk.Checkbutton(root, text="Burger", variable=var2, onvalue=1, offvalue=0)
check2.pack()

button = tk.Button(root, text="Order", command=clickorder)
button.pack()

root.mainloop()
