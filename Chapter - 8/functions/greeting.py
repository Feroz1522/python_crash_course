def get_formatted(first_name,last_name):
    full_name = first_name + ' ' +last_name
    return full_name.title()

while True:
    print("\tenter 'q' anywhere you need to quit") 
    print("\n enter your first name ")
    
    f_name = input('>> ').lower()
    if f_name == 'q':
        break

    print("\n enter your last name ")
    l_name = input('>> ').lower()
    if l_name == 'q':
        break

    Full_name = get_formatted(f_name,l_name)
    print('\n' + Full_name)
