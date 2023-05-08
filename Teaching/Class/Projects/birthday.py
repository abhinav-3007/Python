import time
import tkinter as tk

def disp():
    text = ""
    for i in message:
        text += i
        txt.set(text)
        label.update()
        time.sleep(.15)
    disp()


groot = tk.Tk()
groot.minsize(900, 600)
groot.title("Happy Birthday!!")

txt = tk.StringVar()
message = "Happy Birthday"
txt.set("")

label = tk.Label(groot, textvariable=txt, height=900, foreground="red", font="Times 60")
button = tk.Button(groot, text="Start", font="Times 10", command=disp)

button.pack()
label.pack()
groot.mainloop()
