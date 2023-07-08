def pizza(*toppings):
    """function for printing the toppings"""
    print('the falvours of toppings are ')
    for topping in toppings:
        print(f" - {topping}")
pizza('donut')
pizza('cheese pasta','gucci','zinger')
