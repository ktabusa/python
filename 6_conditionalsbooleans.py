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
language = 'Java'

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
    print('Evaluated to False')

# video complete 02/18/20
