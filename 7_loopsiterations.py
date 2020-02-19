# Loops and Iterations vid 7
# started 02/18/20

nums = [1, 2, 3, 4, 5]

# for num in nums:
# if num == 3:
# print('Found')
# continue
# print(num)
# this loops through and prints each number in the list
# if looking for the number 3


for num in nums:
    for letter in 'abc':
        print(num, letter)

# this provided every combination of the characters

message = ' '
print(message)

for i in range(1, 11):
    # can including a starting value, but it will not include the last value
    print(i)
# this prints the items up to but not including 10, always starts at 0
print(message)
print(message)

x = 0

while x < 10:
    # can replace the conditional value with a value like 'True'
    # if you enter an infinite loop, you can exit out with control q
    if x == 5:
        break
    print(x)
    x += 1
# this loop will continue until the "while" condition is not met
# this will break when the startin condition is not met
