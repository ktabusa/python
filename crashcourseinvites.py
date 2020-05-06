# Started 04/15/20

dinner_invites = ['anthony bourdain', 'john cena', 'dwayne johnson', 'robin williams']

print(dinner_invites)

print(' ')
for name in dinner_invites:
    print(f'Hi {name.title()}, you are invited to a feast.')

print(' ')
oh_no = dinner_invites.pop().title()
print("I'm sorry to say that " + oh_no + ", was unfortunately not able to attend.")
oh_no = dinner_invites.pop(0).title()
print("I'm sorry to say that " + oh_no + ", was unfortunately not able to attend.")
print(' ')
dinner_invites.append('jimi hendrix')


#
# for name in dinner_invites:
#     print(f"What up? {name.title()}  you want to come to a frozen pizza feast.")
# # fstrings probably way easier

for invitee in dinner_invites:
    print('What up? ' + '{}'.format(invitee.title()) +
          ", you want to come to a frozen pizza feast. \n")


# test why won't this statement work:
# for i in dinner_invites:
#     print('What up? ' + '{}'.format(dinner_invites[1].title()) +

pizzas = ['pepperoni', 'hawaiian', 'veggie', 'sausage']

for pizza in pizzas:
    print('I like ' + pizza.title() + ' pizza.\n')

print('I really love pizza!')

print('\nTwo for Loops produce:')
squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)

print(squares)

exponents = []
for value in range(1, 11):
    exponents.append(value**2)

print(exponents)
# both of these can be used, use the one clearest to you and to others


squares2 = [value ** 2 for value in range(1, 11)]
print(squares2)

# test examples for chapter 4, 4-3 to 4-9


# 4-4
million = [value for value in range(1, 1000001)]
# print(million)


print(min(million))
print(max(million))
print(sum(million))

twenty = []
for num in range(1, 21):
    twenty.append(num)
print(twenty)
print('Odd Numbers from 1-10')
print(twenty[:11:2])

odd_numbers = list(range(1, 21, 2))
print(odd_numbers)

for odd in odd_numbers:
    print(odd)


# cubes 4-8
cubes = []
for cube in range(1, 11):
    cubes.append(cube**3)
print(cubes)

for val in cubes:
    print(val)

# slicing lists in crash course


print('Age if - elif - else Testing')
age = 12
if age < 4:
    price = 0
elif age < 12:
    price = 5
else:
    price = 10

# print("Your admission cost is $" + str(price) + ".")
print(f'Your admission price is ${price}.')
