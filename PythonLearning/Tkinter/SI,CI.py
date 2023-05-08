import tkinter as tk


def presscalc():
    try:
        princ = int(pentry.get())
        rate = int(rentry.get())
        time = int(tentry.get())
        print(princ, rate, time)
        intr = 0
        amt = 0
        ans = ""
        print(var)
        if var.get() == 1:
            intr = float("{0:.2f}".format((princ*rate*time)/100))
            amt = "{0:.2f}".format(intr+princ)
            print(intr,amt)
        elif var.get() == 2:
            amt = float("{0:.2f}".format((princ*(1+(rate/100))**time)))
            intr = "{0:.2f}".format(amt-princ)
        ans = f"Interest: {intr}\nAmount: {amt}"
        popup = tk.Toplevel()
        popup.title("Answer")
        label = tk.Label(popup, text = ans)
        label.pack()
    except ValueError as ve:
        print("Value error:", ve)
        error.set("Enter only Numbers")
    except SyntaxError as se:
        print("Syntax error:", se)
        error.set("Please enter values properly")
    except Exception as exe:
        print("Unknown error", exe)
        error.set("Invalid entry")


root = tk.Tk()
root.title("Intrest Finder")

plabel = tk.Label(root,text ="Principal: ")
rlabel = tk.Label(root,text= "Rate: ")
tlabel = tk.Label(root,text= "Time: ")

plabel.grid(row= 1, column = 1)
rlabel.grid(row= 2, column = 1)
tlabel.grid(row= 3, column = 1)

pentry = tk.Entry(root)
rentry = tk.Entry(root)
tentry = tk.Entry(root)

pentry.grid(row = 1, column = 2)
rentry.grid(row = 2, column = 2)
tentry.grid(row = 3, column = 2)

var = tk.IntVar()
radio1 = tk.Radiobutton(root, text= "Simple Interest", variable = var, value = 1)
radio2 = tk.Radiobutton(root, text= "Compound Interest", variable = var, value = 2)

radio1.grid(row = 4, columnspan = 3)
radio2.grid(row = 5, columnspan = 3)

calc = tk.Button(root, text= "Calculate", command = presscalc)
calc.grid(row = 6, columnspan = 3)

error = tk.StringVar()
error.set("")

erlabel = tk.Label(root, textvariable = error)
erlabel.grid(row = 7, columnspan = 3)

root.mainloop()
