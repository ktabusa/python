# started on 04/16/20


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# this method adds the n values from the list above to the new list
# I want the 'n' for each 'n' in nums

# for loop list
# my_list = []
# for n in nums:
#     my_list.append(n)


# List Comprehension method
# the list is, all values of n, for all n values in nums
# my_list = [n for n in nums] (provides the list above)

# we can modify the values of n, ie. n * n or as below
my_list = [n**2 for n in nums]

print(my_list)
# this can be an alternative to maps and lambdas

# I want 'n' for each 'n' in nums, if 'n' is even

# normal list generation
even_list = []
for n in nums:
    if n % 2 == 0:
        even_list.append(n)
print(even_list)

# % is modulus
# the n  % 2 provides only the remainder of division, and if = 0 is even

print('reminder = 3 % 2 is 1')
print(3 % 2)

print(' ')
even_compr = [n for n in nums if n % 2 == 0]
# this list is n, for n values in the numset IF n mod 2 is 0 (number even)
print(even_compr)

# for loop list
ab = []
for letter in 'abcd':  # comments inline?
    for num in range(4):
        ab.append((letter, num))
print(ab)
# list comp method
# this is is value, value, for
abcomp = [(letter, num) for letter in 'abcd' for num in range(4)]
print(abcomp)
# note: this will run as many times as list has values
# the values describing letter num, need to match the values in the for
# the same values must be used across the list comprehension


# dictionary comprehensions = YT video timestamp 11:40
print('\nDictionary Comprehensions')


alias = ('Bruce', 'Clark', 'Peter', 'Logan', 'Wade')
hero = ('Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool')

# hero_zip = list(zip(alias, hero))
# print(hero_zip)

# print(zip(alias, hero)) this returns a list of paired tupes in Python2
# for python 3 the zip fucntion returns an iterator,
# # zip() is a new function

# I want a dictionary, {'alias': 'hero'} for each alias,hero in zip(alias,hero)
# alias will be the key, and the hero will the value
# to create a dictionary, with for loops

# hero_dict = {}
# for name, hero in list(zip(alias, hero)):
#     hero_dict[name] = hero
# print(hero_dict)


# Dictionary Comprehension time

my_dict = {alias: hero for alias, hero in list(zip(alias, hero))}
print(my_dict)

# can also add additional if statements to the list
# if alias != 'Clark' can be tacked on after the 'in'

# note: when running both the list and the dictionary constructions,
# the hero variables were used twice and overlapped


# Set comprehensions @ 14:10
# also has information on generators...

squares = []
# for n in range(1, 11):
#     value = n**2
#     squares.append(value)
# print(squares)

for n in range(1, 11):
    squares.append(n**2)
print(squares)

# completed 4/16/20
