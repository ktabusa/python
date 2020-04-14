# slicing of lists and strings
# started on 02/25/20

# list[start:end:step]
# the end value is non-inclusive

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9          the corresponding indices
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1      the corresponding indices

print(my_list[0:8])
# prints the entire list from 0 to the eigth position, but not including

print(my_list[2:-1:2])
# alternating numbers if the step is 2

print(my_list[-1:2:-2])
# in reverse from '8' to 2, the '1' in the second position is not included
# alternating numbers but in reverse

print(my_list[::-1])
# can use ':' with nulls preceding or following for a generic start/end

message = ' '
print(message)
print(message)

sample_url = 'http://coreyms.com'
print(sample_url)

# Reverse the url
print(sample_url[::-1])
# this leaves the start and end empty, using the whole list
# and prints it in reverse


# # Get the top level domain
print(sample_url[-4:])
# to get the '.com' domain we can pull the -4 as the start
# and use a null to print all info until the end
print(message)

# # Print the url without the http://
print(sample_url[7:])
# the 'http://'' is comprised of the first 7 chars fo the sample

# # Print the url without the http:// or the top level domain
print(sample_url[7:-4])
# snips off the http and .com info by printing the middle

# completed 02/25/20

# index = my_list.index('3')
