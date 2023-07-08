def get_formatted(firstname,lastname):
    """ program for showing first and last """  
    full_name = firstname +' '+ lastname
    return full_name.title()

name = get_formatted('feroz','khan')
print(name)
