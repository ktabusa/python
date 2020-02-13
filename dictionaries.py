
# Dictionaries
# aka key value pairs, hashmaps, or associative arrays
# creating a student dictionary

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
# key comes first, value comes second


print(student)
print(student['name'])
print(student['courses'])

message = ' '
print(message)


# if you try to print a value that doesn't exist, and error is returned
# can use .get to show "None" as the returned vallue
print(student.get('name'))

print(student.get('phone'))
print(student.get('phone', 'Not Found'))
# if you use a second argument to the .get method


# student['phone'] = '555-5555'
# you can update a dictionary value
print(student.get('phone'))

# student['name'] = 'Jane'

print(student)
# 'Jane' replaced 'John' in the name field for the dictionary
# can use the .update method to change a dictionary
print(message)
student.update({'name': 'Jane', 'age': 27, 'phone': '555-5551'})
print(student)

del student['courses']
print(student)

age = student.pop('age')
print(student)
print(age)
# this popped off the age value from the age dictionary

print(len(student))
# shows the number of keys in the dictionary
print(student.keys())
print(student.values())
print(student.items())
# .items shows the key / value pairs. ie name-John, phone-555...

print(message)
# for key in student:
#   print(key)
for key, value in student.items():
    print(key, value)
# complete 02/13/20
