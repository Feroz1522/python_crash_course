def print_models(unprinted_models,completed_models):
    print('we copied the stuffs')
    while unprinted_models:
        completed = unprinted_models.pop()
        completed_models.append(completed)

unprinted_models = ['demo','car case','iphone case']
completed_models =[]

