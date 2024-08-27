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

# Modifiying elements from a list
garden_waitlist = ["Jiho", "Adam", "Sonny", "Alisha"]
garden_waitlist[1] = "Calla"

print(garden_waitlist)

garden_waitlist[-1] = "Alex"
print(garden_waitlist)

# Remove object from list: 
order_list = ["Celery", "Orange Juice", "Orange", "Flatbread"]
print(order_list)

order_list.remove("Flatbread")
print(order_list)

new_store_order_list = ["Orange", "Apple", "Mango", "Broccoli", "Mango"]

print(new_store_order_list)

new_store_order_list.remove("Mango")
print(new_store_order_list)

new_store_order_list.remove("Onions")

# Two-Dimensional (2D) Lists

heights = [["Jenny", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64], ["Vik", 68]]

ages = [["Aaron", 15], ["Dhruti", 16]]