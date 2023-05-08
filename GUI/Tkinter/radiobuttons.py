import tkinter as tk


def clickorder():
    message = "Your order is "
    if var1.get() == 1:
        message += "Pizza"
    elif var1.get() == 2:
        message += "Burger"
    else:
        message = "You have no order"
    popup = tk.Toplevel()
    label2 = tk.Label(popup, text=message)
    label2.pack()
    var1.set(0)


root = tk.Tk()

label = tk.Label(root, text="What to eat?")
label.pack()
root.title("Menu")

var1 = tk.IntVar()
radio1 = tk.Radiobutton(root, text="Pizza", variable=var1, value=1)
radio1.pack()

radio2 = tk.Radiobutton(root, text= "Burger", variable= var1, value= 2)
radio2.pack()

button = tk.Button(root, text = "Order", command= clickorder)
button.pack()

root.mainloop()
