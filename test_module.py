# created as a test module for (9_import_modules...)

print('Imported my_module...')
# when this is imported into another document, it will also be run

test = 'Test String'


def find_index(to_search, target):
    '''Find the index of a value in a sequence'''
    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1
