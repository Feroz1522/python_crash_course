def print_models(unprinted_designs,completed_models):
    """ this function is for changing the complete list"""
    print("THE DESIGNS NEEDED TO BE PRINTED")
    while unprinted_designs:
        printed_designs = unprinted_designs.pop()
        print("-",printed_designs)
        completed_models.append(printed_designs)
        
def show_completed_model(completed_models):
    """ this function is used for printing the completed models """
    print('THE PRINTED DESIGNS ARE : ')
    for completed_model in completed_models:
        print("-",completed_model)

unprinted_designs = ['back case','car models','laptop tabel ']
completed_models = []
print_models(unprinted_designs,completed_models)
show_completed_model(completed_models)
