# Object Oriented Programming Tutorial 1
# Classes and Instances
# start 03/02/20

# can us a pass statement if you want to leave a class empty

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
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return ('{} {}'.format(self.first, self.last))
# aways need to include the self argument

# class using 1.04 in the apply_raise method is an option
# but class variables are easier to update
#     self.pay = int(self.pay * 1.04)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
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
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

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
