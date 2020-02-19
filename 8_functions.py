# Functions vid 8
# created  02/18/20


def hello_func():
    #     pass
    # if the function is blank, it will show errors, pass keyword is a placeholder
    return 'Hello Function.'

# print(hello_func())
# if you print the function, it prints the function and includes a location
# if you include () it will print 'None' because there are no return values


# hello_func()
# hello_func()
# hello_func()
# hello_func()
# keeping code dry, this instead of print('Hello Function!')
# prevents the need to change multiple locations

print(len('Test'))
# 6:20 in the vid

# print(hello_func().upper())
# can string methods like, .upper on the function


def hello_func(greeting, name='User'):
    return'{}, {}'.format(greeting, name)


print(hello_func('Hi'))

message = ' '
print(message)
print(message)
# this printout uses the default value in the 'name' field
# print(hello_func('Hi', name='Corey'))
# the required positonal arguments need to come before the keyword arguments


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

# accepts an arbitrary number of positional or keyword arguments
# args and kwargs are conventional

# student_info('Math', 'Art', name='John', age=22)

# this creates a tuple with all of the positional arguments
# kwargs is a dictionary with all of the keyword values


courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}
# tuple (), list [], dictionary {},

# student_info(courses, info)
# this passes in the complete list and dictionary as positional args

student_info(*courses, **info)

print(message)
print(message)
print(message)
print(message)
print('Leap Year Function Start')

# these are functions from the python standard library
# snippets taken from his video

# 15:48 in vid
# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""
# triple quotes are called a docstring, document what a function or
# class is supposed to do,

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
# this is how leap years are determined


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]


print(is_leap(2017))
print(is_leap(2020))

print(message)

print(days_in_month(2017, 2))
print(days_in_month(2020, 2))
print(days_in_month(2020, 13))
