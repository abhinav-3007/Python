import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.resizable(False, False)

equation = tk.StringVar()
equation.set("")
expression = ""


def click(num):
    global expression
    expression += num
    equation.set(expression)


def equal():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
    except ZeroDivisionError as ze:
        print("ZeroDivisionError", ze)
        equation.set("ERROR")
    except SyntaxError as se:
        print("SyntaxError:", se)
        equation.set("SYNTAX ERROR")
    except ValueError as ve:
        print("ValueError:", ve)
        equation.set("ERROR")
    except Exception as ex:
        print("Exception:", ex)
        equation.set("ERROR")
    finally:
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set(expression)


dispbox = tk.Entry(root, textvariable=equation, state=tk.DISABLED, font=("", 20))
dispbox.grid(row=0, columnspan=4, padx=10, pady=10, ipadx=85, ipady=10)

button1 = tk.Button(root, text=" 1 ", command=lambda: click("1"), height=2, width=7)
button1.grid(row=2, column=0, padx=10, pady=10)

button2 = tk.Button(root, text=" 2 ", command=lambda: click("2"), height=2, width=7)
button2.grid(row=2, column=1, padx=10, pady=10)

button3 = tk.Button(root, text=" 3 ", command=lambda: click("3"), height=2, width=7)
button3.grid(row=2, column=2, padx=10, pady=10)

plus = tk.Button(root, text=" + ", command=lambda: click("+"), height=2, width=7)
plus.grid(row=2, column=3, padx=10, pady=10)

button4 = tk.Button(root, text=" 4 ", command=lambda: click("4"), height=2, width=7)
button4.grid(row=3, column=0, padx=10, pady=10)

button5 = tk.Button(root, text=" 5 ", command=lambda: click("5"), height=2, width=7)
button5.grid(row=3, column=1, padx=10, pady=10)

button6 = tk.Button(root, text=" 6 ", command=lambda: click("6"), height=2, width=7)
button6.grid(row=3, column=2, padx=10, pady=10)

minus = tk.Button(root, text=" - ", command=lambda: click("-"), height=2, width=7)
minus.grid(row=3, column=3, padx=10, pady=10)

button7 = tk.Button(root, text=" 7 ", command=lambda: click("7"), height=2, width=7)
button7.grid(row=4, column=0, padx=10, pady=10)

button8 = tk.Button(root, text=" 8 ", command=lambda: click("8"), height=2, width=7)
button8.grid(row=4, column=1, padx=10, pady=10)

button9 = tk.Button(root, text=" 9 ", command=lambda: click("9"), height=2, width=7)
button9.grid(row=4, column=2, padx=10, pady=10)

multiply = tk.Button(root, text=" x ", command=lambda: click("*"), height=2, width=7)
multiply.grid(row=4, column=3, padx=10, pady=10)

ac = tk.Button(root, text=" AC ", command=clear, height=2, width=7)
ac.grid(row=5, column=0, padx=10, pady=10)

button0 = tk.Button(root, text=" 0 ", command=lambda: click("0"), height=2, width=7)
button0.grid(row=5, column=1, padx=10, pady=10)

e = tk.Button(root, text=" = ", command=equal, height=2, width=7)
e.grid(row=5, column=2, padx=10, pady=10)

divide = tk.Button(root, text=" / ", command=lambda: click("/"), height=2, width=7)
divide.grid(row=5, column=3, padx=10, pady=10)

exp = tk.Button(root, text=" ^ ", )

root.mainloop()
