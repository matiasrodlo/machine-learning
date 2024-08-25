# Introduction to Lists

heights = [61, 70, 67, 64, 65]

broken_heights = [65, 71, 59, 62]

# List elements

ints_and_strings = [1, 2, 3, "four", "five", "hola"]

sam_height_and_testscore = ["Sam", 67, 85.5, True]

# Empty list

my_empty_list = []

# Append

orders = ["daisies", "periwinkle"]

print(orders)

orders.append("tulips")
orders.append("roses")
print(orders)

# Growing a List: Plus (+)

orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]

# Create new orders here:
new_orders = orders + ["lilac", "iris"]
orders_combined = orders + new_orders

broken_prices = [5, 3, 4, 5, 4] + [4]