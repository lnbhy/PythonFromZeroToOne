def get_formatted_name(first, last):
    '''Returns a string with the full name in Last First format.'''
    first = first.title()
    last = last.title()
    return "{} {}".format(first, last)