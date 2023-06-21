sandwich_orders = ['cheese sandwich','pastrami','mexican sandwich','pastrami',
        'crispy sandwich','pastrami','special sandwich']
finished_sandwiches = []

#telling customers that we are out of pastrami
print("we are out of pastrami sandwich")

#removing pastrami from list
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    print(f"we finished your order {sandwich_order}")
    finished_sandwiches.append(sandwich_order)

print("this are the orders we made today")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
