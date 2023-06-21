sandwich_orders = ['cheese sandwich','mexican sandwich','crispy sandwich','special sandwich']
finished_sandwiches = []

while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    print(f"we finished your order {sandwich_order}")
    finished_sandwiches.append(sandwich_order)

print("this are the orders we made today")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
