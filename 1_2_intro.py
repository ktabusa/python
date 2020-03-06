# Intro and Strings Video 1 & 2
# Print Welcome Message


print('Test')

message = """Hello World
Today is a good day."""


print(message)
# Can use len() to count characters
print(len(message))


print(message[12:32])
print(message[12:32].upper())

# .lower also works
print(message.count('d'))
# count counts all of 'x' but is case specific
print(' ')

new_message = message.replace('World', 'Boss')

print(new_message)


message = new_message
print(message)


print(" ")

greeting = 'Hello'
name = 'Keenan'

message = f'{greeting}, {name}. Welcome!'

message = greeting + ', ' + name + '. Welcome!'

message = '{}, {}. Welcome!'.format(greeting, name)

# the pluses, {}, and 'f' all work the same

print(message)

# 17:38 in second video

print(dir(name))
# Print Welcome Message

print('mragghhhh')

message = """Hello World
Today is a good day.
To Die"""


print(message)

# Can use len() to count characters
print('word count')
print(len(message))


print(message[12:32])
print(message[12:32].upper())

# .lower also works
print(message.count('d'))
# count counts all of 'x' but is case specific
print('--linebreak--')

new_message = message.replace('World', 'Boss')

print(new_message)


message = new_message

print("--linebreak for new message replacement")

print(message)

greeting = 'Hello'
name = 'Keenan'

message = f'{greeting}, {name}. Welcome!'

message = greeting + ', ' + name + '. Welcome!'

message = '{}, {}. Welcome!'.format(greeting, name)

# the pluses, {}, and 'f' all work the same

print(message)

# 17:38 in second video

print(dir(name))

# toggling softwrap is not working

print(help(str))
# print(help(str.replace))
