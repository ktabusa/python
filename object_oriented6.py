# OOP 6 started  04/10/20
# Property Decorators - getters, setters, and deleters
# pared down the Employee class to speed this up


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = first + '.' + last + '@company.com'

    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return ('{} {}'.format(self.first, self.last))

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Deleted Name!')
        self.first = None
        self.last = None


emp_1 = Employee('Keenan', 'Tabusa')

# emp_1.first = 'Keens'

emp_1.fullname = 'Jon Snow'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
# does not change the email, but updates fullname bc it initiates a new pull

# updating the email here to create a method will BREAK PREVIOUS code,
# when we update the email call to a method, we need to update the parens
# throughout all previous code from, print emp_1.email, to emp_1.email()
# can use a property decorator - @property

print(' ')
del emp_1.fullname
print(emp_1.first)
print(emp_1.last)
