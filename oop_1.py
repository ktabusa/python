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


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return ('{} {}'.format(self.first, self.last))
# aways need to include the self argument


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
