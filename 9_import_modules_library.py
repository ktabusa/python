# Functions vid 9
# started  02/19/20

# print('Imported my_module...')
#
# test = 'Test String'
#
#
# def find_index(to_search, target):
#     '''Find the index of a value in a sequence'''
# # this searches the first argument and searches the list for the targ
#
#     for i, value in enumerate(to_search):
#         if value == target:
#             return i
#
#     return -1
#
# # this is a test script kept in a the test_module side doc


import os
import calendar
import datetime
import math
import random
import sys
from test_module import find_index, test
courses = ['History', 'Math', 'Physics', 'CompSci']
# import test_module as tm
# index = test_module.find_index(courses, 'Math')
# if you import as '__' it will not be know as the full name
# index = tm.find_index(courses, 'Physics')

index = find_index(courses, 'Physics')
print(index)
# if you use the from test_module import find_index, it only brings
# the find_index function and not any other variables,
print(test)

# you can use the 'from test_module import *' however this is unclear and lazy

# when you import a module, it checks the list sys.path

# print(sys.path)
# this path contains, the location of the script we're running first
# next it contains the python path environment variable
# next adds the standard library directories
# last the site packages directories

# see vid @ 9:50 mark to see how to change the python path envi variable


message = ' '
print(message)
print('Testing Random Import')

random_course = random.choice(courses)
print(random_course)
# uses a standard library random module to pull a random variable from our list
# this bumped up 'import random' to the top

print(message)
print(message)
print(message)


print('Math Calcs')
# this bumped up 'import random' to the top

rads = math.radians(90)
print(rads)

# this bumped up 'datetime' and import 'calendar' to the top

print('Calendar')
today = datetime.date.today()
print(today)
print(calendar.isleap(2017))

print(message)
print(message)
# kicked 'import os' to the top
print('OS Test')

print(os.getcwd())
# can find the file location
print(os.__file__)
# dunder = __
