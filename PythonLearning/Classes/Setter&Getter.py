class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    @property
    def fullname(self):
        return self.first+" "+self.last
    # This creates getter for email function
    @property
    def email(self):
        return f"{self.first}{self.last}@abhinav.com"
    # This creates setter for fullname
    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split()

    def __repr__(self):
        return f"Employee[Name: {self.fullname}; Salary: {self.salary}]"

    def __str__(self):
        return "<class 'Employee'>"

    def __add__(self, other):
        return self.salary + other.salary
#
#
# class Developer(Employee):
#     def __init__(self, first, last, salary, prog_lang):
#         super().__init__(first, last, salary)
#         self.prog_lang = prog_lang
#
#     def __repr__(self):
#         return f"Developer[Name: {self.fullname}; Salary: {self.salary}; prog_lang{self.prog_lang}]"
#
#     def __str__(self):
#         return "<class 'Developer'>"
#
#
# class Manager(Employee):
#     def __init__(self, first, last, salary, emp_list = None):
#         super().__init__(first, last, salary)
#         if emp_list == None:
#             self.list_of_emp = []
#         else:
#             self.list_of_emp = emp_list
#
#     def add_emp(self, emp):
#         self.list_of_emp.append(emp)
#
#     def remove_emp(self, emp):
#         if emp in self.list_of_emp:
#             self.list_of_emp.remove(emp)
#         else:
#             print("Employee not found")
#
#     def all_emp(self):
#         for i in self.list_of_emp:
#             print(i.fullname())
#
#     def __repr__(self):
#         return f"Manager[Name: {self.fullname}; Salary: {self.salary}; emp_list: {self.list_of_emp}]"
#
#     def __str__(self):
#         return "<class 'Manager'>"
#
#
# dev1 = Developer("Raghav", "Mehra", 1, "C++")
# dev2 = Developer("Bob", "Builder", 5, "Python")
# man1 = Manager("Abhinav", "Goyal", 10, [dev1, dev2])
emp1 = Employee("Ching", "Chang", 100)
#
# man1.remove_emp(dev1)

emp1.fullname = "Chang Ching"

# man1.all_emp()
#
# print(emp1+man1)

print(emp1.fullname)