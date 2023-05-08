import tkinter as tk
import re

message = []
count = 0


def press_sign():
    global message
    global count
    count = 0
    message.clear()
    user.config(bg="white")
    first.config(bg="white")
    last.config(bg="white")
    age.config(bg="white")
    city.config(bg="white")
    email.config(bg="white")
    phone.config(bg="white")

    user_ = user.get()
    first_ = first.get()
    last_ = last.get()
    age_ = age.get()
    city_ = city.get()
    email_ = email.get()
    phone_ = phone.get()

    userpattern = re.compile(r"[\w&$-]{6,20}")
    namepattern = re.compile(r"[A-Z][a-z]+")
    agepattern = re.compile(r"[0-9]{1,2}")
    emailpattern = re.compile(r"[\w.-]+@[a-z-]+\.[a-z]{2,3}")
    phonepattern = re.compile(r"[9876][\d]{9}")

    if not userpattern.match(user_):
        count += 1
        message.append("Invalid User Id")
        user.config(bg="red")
    if not namepattern.match(first_):
        count += 1
        message.append("Invalid First Name")
        first.config(bg="red")
    if not namepattern.match(last_):
        count += 1
        message.append("Invalid Last Name")
        last.config(bg="red")
    if not namepattern.match(city_):
        count += 1
        message.append("Invalid City Name")
        city.config(bg="red")
    if not agepattern.match(age_):
        count += 1
        message.append("Invalid Age")
        age.config(bg="red")
    if not emailpattern.match(email_):
        count += 1
        message.append("Invalid Email Address")
        email.config(bg="red")
    if not phonepattern.match(phone_):
        count += 1
        message.append("Invalid Phone Number")
        phone.config(bg="red")

    if count != 0:
        display.config(text="\n".join(message), fg="red")
    else:
        display.config(text=f"Hello {user_}!\nYou have successfully signed up!", fg="black")


def press_clear():
    user.delete(0, "end")
    first.delete(0, "end")
    last.delete(0, "end")
    age.delete(0, "end")
    city.delete(0, "end")
    email.delete(0, "end")
    phone.delete(0, "end")


root = tk.Tk()

root.title("login page")
root.geometry('250x325')
root.resizable(False, False)

label1 = tk.Label(root, text="User Id: ")
label2 = tk.Label(root, text="First Name: ")
label3 = tk.Label(root, text="Last Name: ")
label4 = tk.Label(root, text="Age: ")
label5 = tk.Label(root, text="City: ")
label6 = tk.Label(root, text="Email: ")
label7 = tk.Label(root, text="Phone No.: ")

user = tk.Entry(root)
first = tk.Entry(root)
last = tk.Entry(root)
age = tk.Entry(root)
city = tk.Entry(root)
email = tk.Entry(root)
phone = tk.Entry(root)

sign = tk.Button(root, text="Sign Up", command=press_sign)
clear = tk.Button(root, text="Clear", command=press_clear)

display = tk.Label(root)

label1.grid(column=1, row=1)
label2.grid(column=1, row=2)
label3.grid(column=1, row=3)
label4.grid(column=1, row=4)
label5.grid(column=1, row=5)
label6.grid(column=1, row=6)
label7.grid(column=1, row=7)

user.grid(column=2, row=1)
first.grid(column=2, row=2)
last.grid(column=2, row=3)
age.grid(column=2, row=4)
city.grid(column=2, row=5)
email.grid(column=2, row=6)
phone.grid(column=2, row=7)

sign.grid(column=2, row=8)
clear.grid(column=2, row=9)

display.grid(column=2, row=10)

root.mainloop()
