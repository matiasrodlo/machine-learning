# First user wants to travel between these two points!
print("Setting the Empire State Building as the starting point and Times Square as our destination.")
print("Calculating the total distance between our points.") 
print("The best route is by train and will take approximately 10 minutes.") 

# Second user wants to travel between these two points!
print("Setting the Empire State Building as the starting point and Times Square as our destination.")
print("Calculating the total distance between our points.") 
print("The best route is by train and will take approximately 10 minutes.") 

# Third user wants to travel between these two points!
print("Setting the Empire State Building as the starting point and Times Square as our destination.")
print("Calculating the total distance between our points.") 
print("The best route is by train and will take approximately 10 minutes.") 

# Fourth user wants to travel between these two points!
print("Setting the Empire State Building as the starting point and Times Square as our destination.")
print("Calculating the total distance between our points.") 
print("The best route is by train and will take approximately 10 minutes.") 

# Defining a function

def directions_to_timesSq():
  print("Walk 4 mins to 34th St Herald Square train station")
  print("Take the Northbound N, Q, R, or W train 1 stop")
  print("Get off the Times Square 42nd Street stop")

  def directions_to_timesSq():
  print("Walk 4 mins to 34th St Herald Square train station.")
  print("Take the Northbound N, Q, R, or W train 1 stop.")
  print("Get off the Times Square 42nd Street stop.")
  print("Take lots of pictures!")

# Calling a Function:
directions_to_timesSq()

# Whitespace and Execution flow

print("Checking the weather for you!")

def weather_check():
  print("Looks great outside! Enjoy your trip.")
print("False Alarm, the weather changed! There is a thunderstorm approaching. Cancel your plans and stay inside.")

weather_check()

# Parameters & Arguments

def generate_trip_instructions(location):
  print("Looks like you are planning a trip to visit " + location)
  print("You can use the public subway system to get to " + location)

generate_trip_instructions("Grand Central Station")

# Multiples paramenters

def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
  car_rental_total = car_rental_rate * trip_time  
  hotel_total = hotel_rate * trip_time - 10
  trip_total = car_rental_total + hotel_total + plane_ticket_price
  return trip_total

# Step 5: call your function

print(calculate_expenses(200, 100, 100, 5))

# Type of arguments

def trip_planner(first_destination, second_destination, final_destination="Codecademy HQ"):
  print("Here is what your trip will look like!")
  print("First, we will stop in " + first_destination + ", then " + second_destination + ", and lastly " + final_destination)

trip_planner("France", "Germany", "Denmark")
trip_planner("Denmark", "France", "Germany")
trip_planner(first_destination="Iceland", final_destination="Germany", second_destination="India")
trip_planner("Brooklyn", "Queens")

# Build in function in python

tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00

# Write your code below:
max_price = max(tshirt_price, shorts_price, mug_price, poster_price)
min_price = min(tshirt_price, shorts_price, mug_price, poster_price)
rounded_price = round(tshirt_price, 1)
print(max_price)
print(min_price)
print(rounded_price)

# variable scope
favorite_locations = "Paris, Norway, Iceland"

def print_count_locations():
  print("There are 3 locations")
    
# Returns       
def show_favorite_locations():
  print("Your favorite locations are: " + favorite_locations)

print_count_locations()
show_favorite_locations()

current_budget = 3500.75

def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget))

print_remaining_budget(current_budget)

# Write your code below: 
def deduct_expense(budget, expense):
  return budget - expense
shirt_expense = 9
new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)

print_remaining_budget(new_budget_after_shirt)

# Multiples returns

def top_tourist_locations_italy():
  first = "Rome"
  second = "Venice"
  third = "Florence"
  return first, second, third

most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()

print(most_popular1)
print(most_popular2)
print(most_popular3)