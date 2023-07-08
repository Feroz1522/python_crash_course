def make_pizza(name,*toppings):
    """ this function is used for making the pizza """
    print(f" \nOrder for {name} is :")
    for topping in toppings :
        print(f' - {topping}')

