# Conditionals and Booleans Video 6

if True:
    print('Conditional was True')

# if False:
#     print('Conditional was True')
message = ' '

# notes taken from integers..
# Comparisons:
# Equal:                3 == 2
# Not Equal             3 != 2
# Greater Than:         3 > 2
# Less Than:            3 < 2
# Greater or Equal:     3 >= 2
# Less or Equal:        3 <= 2
# Object Identity:      is


print(message)
# language = 'Python'
language = 'Python'

if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
elif language == 'JavaScript':
    print('Language is JavaScript')
else:
    print('No Language Match')

# Python does not have a switch case, because if, elif, and else suffice
# additional elif functions work the same

print(message)
print(message)

# Booleans
# and
# or
# not


user = 'Admin'
logged_in = False

# we can use this to only execute codeif the user is admin, and logged

if user == 'Admin' and logged_in:
    print('Admin Page')
if not logged_in:
    print("Please Log In")
else:
    print('Bad Credential Page')
# 7:28

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(id(a))
print(id(b))
# the id's for these two lists is different,
# if "b=a", then the lists would have the same id

print(a is b)
print(message)

# False Values:
# False
# None
# Zero of any numeric type
# Any empty sequence. For example, '', (), [].
# Any empty mapping. For example, {}.
# if a number is not '0', then this will eval to true

condition = {}

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False\n')

# video complete 02/18/20


# additional if elif else condition testing form the crash course

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pineapple', 'pepperoni']
requested_toppings = ['mushrooms', 'french fries', 'green peppers']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we are out of " + requested_topping + " right now.")
# this only works if one item is not in the list, if there are more, update

# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms.")
# if 'pepperoni' in requested_toppings:
#     print('Adding pepperoni.')
# if 'extra cheese' in requested_toppings:
#     print("Adding Extra Cheese."

print("\nFinished making you Pizza!")


print("Alien Colors")
alien_color = 'green'
if alien_color is 'green':
    print("Player earned 5 points")
elif alien_color != 'green':
    print("Player earned 10 Points")

print('\nStages of Life')
age = 20


if age < 2:
    print('person is a baby')
elif age >= 2 and age < 4:
    print('person is a toddler')
elif age >= 4 and age < 13:
    print('person is a kid')
elif age >= 13 and age < 20:
    print('person is a teen')
elif age >= 20 and age < 65:
    print('person is an adult')
