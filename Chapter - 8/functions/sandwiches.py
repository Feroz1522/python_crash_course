def sandwiches(*toppings):
    """ Function for sandwiches """
    print('\nyour orders are :')
    for topping in toppings:
        print(f"\t- {topping}")

sandwiches('pepper')
sandwiches('cheesy','peri peri','arabian','barbique')
