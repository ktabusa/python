# Object Oriented Programming Tutorial 1
# Classes and Instances
# start 03/02/20

# can use a pass statement if you want to leave a class empty

# manually setting variables is a pain
# can auto set up variables with classes
# this is the code the manually set up the variables below
# emp_1.first = 'Keenan'
# emp_1.last = 'Tabusa'
# emp_1.email = 'Keenan.Tabusa@company.com'
# emp_1.pay = '50000'
#
# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = 'Test.User@company.com'
# emp_2.pay = '60000'


import datetime


class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        # Employee.num_of_emps + = 1

    def fullname(self):
        return ('{} {}'.format(self.first, self.last))
# aways need to include the self argument

# class using 1.04 in the apply_raise method is an option
# but class variables are easier to update
#     self.pay = int(self.pay * 1.04)

    def apply_raise(cls):
        cls.pay = int(cls.pay * cls.raise_amt)
# cannot just insert 'raise_amount' instead of 1.04
# you need to definte a class, or instance to apply the r_a to
# can use class (Employee), or instance (self) to apply the r_a

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

# static method from 10:00 of Tutorial3
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Keenan', 'Tabusa', 50000)
emp_2 = Employee('Test', 'User', 60000)


print(emp_1.email)
print(emp_2.email)

message = ' '
print(message)
# this is one, more difficult way to print the first and last name
# print('{} {}'.format(emp_1.first, emp_1.last))

# you can also create a method for the fullname
# the following method was added to the class above to shorten the name pull
# def fullname(self):
#     return ('{} {}'.format(self.first, self.last))

print(emp_1.fullname())
print(message)
print(message)
print(emp_1.fullname())
print(Employee.fullname(emp_1))
# all of these statements are the same

# completed 03/03/20

# OOP Tutorial 2
# Class Variables

print(message)
print('Start Tutorial 2')
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

# using a raise amount will allow easy updates via a class variable
# emp_1.raise_amount()
# Employee.raise_amount()

print(message)
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

print(message)
# to print the namespace of emp_1 you can see all attributes
print(emp_1.__dict__)
# this shows that the raise_amount info is not assigned to an instance
print(Employee.__dict__)

print(message)
print(Employee.num_of_emps)

print(message)
print('Start Tutorial 3')

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

first, last, pay = emp_str_1.split('-')

# new_emp_1 = Employee(first, last, pay)
new_emp_1 = Employee.from_string(emp_str_1)
# this is a from string alternative constructor


print(new_emp_1.pay)
print(new_emp_1.email)

print(message)
print('Workday')
my_date = datetime.date(2016, 10, 14)
print(Employee.is_workday(my_date))

# started OOP 4 04/09/20


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

# didn't take the extra self.first info to keep code clean.
# the employee init method will take the other aspects.
# the super().__init__ will take it.
# can also use Employee.__initi__(self, first, last, pay)
# super is more necessary if you need to use multiple inheritance


dev_1 = Developer('Dev', 'Tomas', 100000, 'Python')
dev_2 = Developer('Devin', 'Javed', 90000, 'Java')

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
#
# print(dev_1.email)
# print(dev_2.prog_lang)

# timestamp =


class Manager(Employee):
    def __init__(self, first, last, pay, reports=None):
        super().__init__(first, last, pay)
        if reports is None:
            self.reports = []
        else:
            self.reports = reports

    def add_reports(self, rpt):
        if rpt not in self.reports:
            self.reports.append(rpt)

    def remove_reports(self, rpt):
        if rpt in self.reports:
            self.reports.remove(rpt)

    def print_reports(self):
        for rpt in self.reports:
            print('-->', rpt.fullname())

# "None" was used for reports because you shouldn't use mutable objects as
# default data types


mgr_1 = Manager('Sue', 'Smith', 120000, [dev_1])
#
# print(mgr_1.email)
#
# mgr_1.add_reports(dev_2)
# mgr_1.print_reports()
#
print(' ')
#
# mgr_1.remove_reports(dev_1)
# mgr_1.print_reports()

print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))
print(' ')
print(issubclass(Developer, Employee))
