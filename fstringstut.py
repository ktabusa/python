# started 04/15/20
# combined lesson from YT video and Crash Course

from datetime import datetime
print('Alternative String Formatting Methods\n')

# % formatting
name = 'Eric'
last = 'Idle'
age = 74
profession = 'comedian'

print("Hello, %s %s. You are %s. You are a %s." % (name, last, age, profession))

# str.format() / cotcatentation
print("Hello, {} {}. You are {}. You are a {}.".format(name, last, age, profession))

# fstrings bb
print(f'Hello, {name} {last}. You are {age}. You are a {profession}.\n')


first_name = 'keenan'
last_name = 'tabusa'

# this can be done with the .format method
# sentence = 'My name is {} {}'.format(first_name, last_name)

sentence = f'My name is {first_name.title()} {last_name.title()}.'

print(sentence)

# can add .title(), .upper() or other modifiers inside fstrings


person = {'name': 'Jenn', 'age': 23}

# this i sthe version with the normal format method
# sentence2 = 'My name is {} and I am {} years old'.format(person['name'], person['age'])

# fstring method
sentence2 = f"My name is {person['name']} and I am {person['age']} years old"
# be careful with single an double quotes

print(sentence2)

# Maths work


# fstrings can apply to math
# calculation = f'4 times 11 is equal to {4*11}'
# print(calculation)


for n in range(1, 5):
    sentence3 = f'The value is {n:02}'
    print(sentence3)

# can format additional fstring infor with a ':'
# this will 'zero pad' the numbers and make them 2 digits, or 4 etc

# floating point values - FLOATS

print('Floating Point Rounding')
pi = 3.14159265

pie = f'Pi is equal to {pi:.5f}'
print(pie)
pie = f'Pi is equal to {pi:.5}'
print(pie)

# can use the colon for formatting, can print 5 deci digits, using a '.5f'
# the . indicates that it's a floating point, 5f for a floating point
# modifying using '.5' rounds to 5 units total. this correctly rounds

print('Bday Test')
birthday = datetime(1986, 10, 14)
# standard datetime format is year, mo day

bday = f'Keenan has a birthday on {birthday}'
print(bday)
print(' ')
bday = f'Keenan has a birthday on {birthday:%B %d, %Y}'
print(bday)


# output here will return the datetime.datetime output 1986-10-14 00:00:00
# can use the datetime format codes, like %B %d %Y
