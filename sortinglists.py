# sorting lists, tuples, and objects
# started 03/0/20

li = [9, 1, 8, 2, 7, 3, 6, 4, 5]

s_li = sorted(li, reverse=True)
# sorted functoin returns a new sorted list, which can be set as a variable
# can use 'reverse=True'
# this function allows us to use any iterable, not just lists

# li.sort()
# the sort method, sorts the list in place and returns 'none'
# can use 'reverse=True'
# this sort method is good for quick stuff, but less flexible than above
# only allows lists

print('Sorted Variable:\t', s_li)
print('Original Variable:\t', li)
# print('Original Variable:\t', )

message = ' '
print(message)


tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
# tup.sort() does not exist
s_tup = sorted(tup)
print('Tuple\t', s_tup)

print(message)
print(message)

di = {'name': 'Corey', 'job': 'programming', 'age': None, 'os': 'Mac'}
s_di = sorted(di)
print('Dict\t', s_di)
# the '\t' aspect of this print function tabs in the resulting tuple

print(message)

li = [-6, -5, -4, 1, 3, 2, ]
s_li = sorted(li)
abs_li = sorted(li, key=abs)
# the key parameter will perform the abs value step before sorting

print(s_li)
print(abs_li)

print(message)

# classes


class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        # the repr method just tells python how we want the function printed
        return '({}, {}, ${})'.format(self.name, self.age, self.salary)


e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 42, 90000)

employees = [e1, e2, e3]
# s_employees = sorted(employees) will provided an error without a key,
# need to use a key to sort non integer info,


def e_sort(emp):
    return emp.salary
# can use name, age, or salary


s_employees = sorted(employees, key=e_sort)
print(s_employees)
