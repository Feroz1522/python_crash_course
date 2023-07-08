def show_magicians(magicians):
    """function for printing the list data""" 
    for magician in magicians:
        print(magician)

def send_messages():
    """function for moving data from one list to another list"""
    while magicians:
        dummy = magicians.pop()
        empty_list.append(dummy)

magicians = ['mom','dad','friends']
empty_list = []

show_magicians(magicians)
send_messages()

print('\t Final data of lists ')
print(magicians)
print(empty_list)
