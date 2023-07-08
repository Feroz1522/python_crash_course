unprinted_models = ['bike','car','duke','house']
printed_models = []

while unprinted_models:
    #
    working_model = unprinted_models.pop()
    print(f'printing models : {working_model}')
    printed_models.append(working_model)
    #
print('\n the printed models')
for printed_model in printed_models:
    print("the printed models are : " + printed_model)








