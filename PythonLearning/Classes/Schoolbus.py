import tkinter as tk

routelist = []
driverlist = []
pickuplist = []
passengerslist = []
timelist = []
busli = []

class Bus:
    global routelist
    global driverlist
    global pickuplist
    global passengerslist
    global timelist

    def __init__(self, route, driver, pickup, passengers, time):
        self.route = route
        self.driver = driver
        self.pickup = pickup
        self.passengers = passengers
        self.time = time

        routelist.append(self.route+"\n")
        driverlist.append(self.driver+"\n")
        pickuplist.append(self.pickup+"\n")
        passengerslist.append(self.passengers+"\n")
        timelist.append(self.time+"\n")

    def remove(self):
        routelist.remove(self.route+"\n")
        driverlist.remove(self.driver+"\n")
        pickuplist.remove(self.pickup+"\n")
        passengerslist.remove(self.passengers+"\n")
        timelist.remove(self.time+"\n")

    @staticmethod
    def all_bus():
        print("Route numbers:", routelist)
        print("Driver names:", driverlist)
        print("Pickup point:", pickuplist)
        print("Number of passengers:", passengerslist)
        print("Pickup time:", timelist)

    @staticmethod
    def number_of_buses():
        print(len(routelist))

bus1 = Bus("87", "khd", "khj", "10", "7:00")
# ----------------Now all Tkinter starts----------------


def presscreate(route, driver, pickup, passengers, time):
    global busli
    busli.append(Bus(route, driver, pickup, passengers, time))
    status.set("Bus Created")


def pressnew():
    rootn = tk.Toplevel()
    rootn.title("Create new bus")
    rootn.resizable(0,0)

    label1 = tk.Label(rootn, text = "Route number: ")
    label2 = tk.Label(rootn, text = "Driver name: ")
    label3 = tk.Label(rootn, text = "Pickup Point: ")
    label4 = tk.Label(rootn, text = "Number of Passengers: ")
    label5 = tk.Label(rootn, text = "Pickup time: ")

    label1.grid(row = 1, column = 1)
    label2.grid(row = 2, column = 1)
    label3.grid(row = 3, column = 1)
    label4.grid(row = 4, column = 1)
    label5.grid(row = 5, column = 1)

    entry1 = tk.Entry(rootn)
    entry2 = tk.Entry(rootn)
    entry3 = tk.Entry(rootn)
    entry4 = tk.Entry(rootn)
    entry5 = tk.Entry(rootn)

    entry1.grid(row=1, column=2)
    entry2.grid(row=2, column=2)
    entry3.grid(row=3, column=2)
    entry4.grid(row=4, column=2)
    entry5.grid(row=5, column=2)

    route = entry1.get()
    driver = entry2.get()
    pickup = entry3.get()
    number = entry4.get()
    time = entry5.get()

    global status
    status = tk.StringVar()
    status.set("")

    statlabel = tk.Label(rootn, textvariable = status)
    statlabel.grid(row = 8, columnspan = 3)

    create = tk.Button(rootn, text = "Create New Bus", command = lambda: presscreate(route, driver, pickup, number, time))
    clear = tk.Button(rootn, text = "Clear All")

    clear.grid(row = 6, columnspan = 3)
    create.grid(row = 7, columnspan = 3)

    rootn.mainloop()


def pressdelete():
    rootdel = tk.Toplevel()
    rootdel.title("Delete buses")

    global var1
    var1 = tk.IntVar()
    check1 = tk.Checkbutton(rootdel, text = "hdsf", variable = var1)
    check1.grid(row = 1, column=1)
    button = tk.Button(rootdel, text = "click", command = show)
    button.grid(row = 2, column = 1)
    rootdel.mainloop()


def pressview():
    rootv = tk.Toplevel()

    routehead = tk.Label(rootv, text= "Route Number", fg = "Red")
    driverhead = tk.Label(rootv, text = "Driver Name", fg = "Red")
    pickuphead = tk.Label(rootv, text= "Pickup Point", fg = "Red")
    passhead = tk.Label(rootv, text= "Number of Passengers", fg = "Red")
    timehead = tk.Label(rootv, text = "Time of Pickup", fg = "Red")

    route = tk.StringVar()
    route.set("".join(routelist))
    routes = tk.Label(rootv, textvariable=route)

    routes.grid(column = 1, row = 1)

    rootv.mainloop()


root = tk.Tk()
root.title("School Bus Management System")
root.resizable(0,0)

heading = tk.Label(root, text = "School Bus Management System", fg = 'Yellow', bg = "Black")
add = tk.Button(root, text = "New Bus", command = pressnew)
remove = tk.Button(root, text = "Remove Existing Bus", command = pressdelete)
view = tk.Button(root, text = "View all Buses", command = pressview)

heading.grid(row = 1, columnspan = 4, ipadx = 40)
add.grid(row = 2, column = 1)
remove.grid(row = 2, column = 2)
view.grid(row = 2, column = 3)
root.mainloop()
