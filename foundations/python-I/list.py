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

# Index of elements

employees = ["Michael", "Dwight", "Jim", "Pam", "Ryan", "Andy", "Robert"]

employee_four = employees[3]
print(employees[4])

# Negative Index

shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]

last_element = shopping_list[-1]
index5_element = shopping_list[5]
print(index5_element)
print(last_element)