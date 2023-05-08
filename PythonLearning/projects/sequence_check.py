import tkinter as tk


def search():
    global var1
    global var2
    global var3
    global entry
    global fibostr
    global sqstr
    global tristr
    try:
        num = int(entry.get())
        fibo = "No"
        sq = "No"
        tri = "No"
        fibostr.set("")
        sqstr.set("")
        tristr.set("")
        fibonacci = [0]
        square = [0]
        triangular = [0]
        if var1.get() == 1:
            i = 1
            while i <= num:
                fibonacci.append(i)
                i = fibonacci[-1] + fibonacci[-2]
            fibonacci.remove(0)
            if num in fibonacci:
                fibo = "Yes"
            fibostr.set("In fibonacci series: "+fibo)
        if var2.get() == 1:
            i = 1
            while i**2 <= num:
                square.append(i**2)
                i+=1
            square.remove(0)
            if num in square:
                sq = "Yes"
            sqstr.set("In square number series: "+sq+"; The index is "+str(square.index(num)+1))
        if var3.get() == 1:
            i = 0
            x = 1
            while i+x <= num:
                triangular.append(i+x)
                x+=1
                i = triangular[-1]
            triangular.remove(0)
            print(triangular)
            if num in triangular:
                tri = "Yes"
            tristr.set("In triangular number series: "+tri+"; The index is "+str(triangular.index(num)))
        entry.delete(0,"end")
        errorvar.set("")
    except ValueError as ve:
        print("ValueError:",ve)
        errorvar.set("Please enter a valid value")
    except Exception as ex:
        print("Exception:",ex)
        errorvar.set("Please enter a valid value")




root = tk.Tk()

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()

fibostr = tk.StringVar()
sqstr = tk.StringVar()
tristr = tk.StringVar()

label = tk.Label(root, text="Enter the number which you would like to find: ")
entry = tk.Entry(root)
label.grid(row=1, column=1)
entry.grid(row=1, column=2)

label2 = tk.Label(root, text="Select which series to search in:")
label2.grid(row=2,columnspan=3)

fibocheck = tk.Checkbutton(root, text="fibonacci series", variable=var1)
squarecheck = tk.Checkbutton(root, text="square numbers series", variable=var2)
tricheck = tk.Checkbutton(root, text="triangular numbers series", variable=var3)
fibocheck.grid(row=3, columnspan=3)
squarecheck.grid(row=4, columnspan=3)
tricheck.grid(row=5, columnspan=3)

search = tk.Button(root, text="Search", command=search)
search.grid(row=6, columnspan=3)

fibolabel = tk.Label(root, textvariable=fibostr)
sqlabel = tk.Label(root, textvariable=sqstr)
trilabel = tk.Label(root, textvariable=tristr)
fibolabel.grid(row=7, columnspan=3)
sqlabel.grid(row=8, columnspan=3)
trilabel.grid(row=9, columnspan=3)

errorvar = tk.StringVar()
error = tk.Label(root, textvariable=errorvar, fg="Red")
error.grid(row=10, columnspan=3)

root.mainloop()
