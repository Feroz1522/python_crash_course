def make_car(manufacturer,model, **info):
    """ this function is used for collecting the info of the car from the user """
    info['manufacturer'] = manufacturer
    info['model'] = model
    return info

car = make_car('toyota','supra',stock = 2000, warranty ='3 Year' )
print(car)
