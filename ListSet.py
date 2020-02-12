courses = ['History', 'Math', 'Physics', 'CompSci']

print(courses)
print(len(courses))

print(courses[2])
# starting point in a list is index 0

print(courses[-1])
# can search for the last item, etc.

print(courses)
print(courses[2:])
# this is called slicing, can do more to skip values etc in a specific vid

courses.append('Art')

print(courses)

courses.insert(0, 'Art1')
print(courses)

courses_2 = ['Pottery', 'Education']

message = ' '
print(message)
print(courses)
print(message)

print(courses)
courses.extend(courses_2)
print(courses[0:])

print(message)
courses.remove('Math')
print(courses)

print(message)
courses.pop()
print(courses)

popped = courses.pop()
print(popped)
# pop removes the last value in a list

print(message)
print(message)
courses.reverse()
print(courses)

courses.sort()
print(courses)

nums = [1, 5, 7, 4, 3]

nums.sort()
print(courses)
print(nums)

print(message)
courses.sort(reverse=True)
nums.sort(reverse=True)
# True needs to be "True" not "true"
print(courses)
print(nums)

# can use "sorted_courses = sorted(courses)" to not alter the original list
print(max(nums))
print(min(nums))
print(sum(nums))


print(courses.index)
# wtf does this do
print(courses.index('CompSci'))
# print(courses.index('Pottery'))
# 'Pottery' was removed by the pop function earlier and an error was returned

print('Art' in courses)

print(message)
# for item in courses:
for index, item in enumerate(courses, start=1):
    print(index, item)
# "item" is a generic placeholder, index is the specific
# normally the index startpoint is 0, but including "start=1" starts at 1

print(message)
print(message)
print(message)

courses = ['History', 'Math', 'Physics', 'CompSci']

course_str = ' - ' .join(courses)
new_list = course_str.split(' - ')

print(course_str)
print(new_list)

# stopped at 20:21 in video
# tuples are like lists, but cannot be modified (immutable)

print(message)
print('Tuples')
print(message)

list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1
# list examples
print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)
print(message)
print(message)

print('Tuples Example')
# Immutable

tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

# to change the tuple with: tuple_1[0] = 'Arts', returns an error function
# can't modify/mutate the tuple with append etc.
print(tuple_1)
print(tuple_2)

print(message)
print(message)
print("Sets Notes")
# Sets have slightly different functionality than lists, Tuples

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}

print(cs_courses)
# the order can change with each execution for the output
# sets don't care about order
# used to test if a value is part of a set, or to remove duplicates

print(message)
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}
print(cs_courses)
print('Math' in cs_courses)
print(message)

print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))

print(cs_courses.union(art_courses))
# can combine and not have duplicates with sets vs lists or tuples..


# Empty Lists
empty_list = []
empty_list = list()


# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
# empty_set = {}  # this isn't right! it's a dictionary
empty_set = set()
