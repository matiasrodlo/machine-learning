# Control Flow:

statement_one = "No"
statement_two = "Yes"
statement_three = "No"
statement_four = "Yes"

# relational operators:

first_expression = True
second_expression = True
third_expression = False

# Boolean variable:

my_baby_bool = "true"
print(type(my_baby_bool))

my_baby_bool_two = True
print(type(my_baby_bool_two))

# If Statement

user_name = "angela_catlady_87"

if user_name == "Dave":
  print("Get off my computer Dave!")
if user_name == "angela_catlady_87":
  print("I know it is you, Dave! Go away!")

# Relational Operators II

x = 20
y = 20

# Write the first if statement here:
if x == y:
  print("These numbers are the same")


credits = 120

# Write the second if statement here:
if credits >= 120:
  print("You have enough credits to graduate!")

# Boolean Operators: and

statement_one = False

statement_two = True

credits = 120
gpa = 3.4

if credits >= 120 and gpa >= 2.0:
  print("You meet the requirements to graduate!")

# Boolean Operators: or

statement_one = True

statement_two = True

credits = 118
gpa = 2.0

if credits >= 120 or gpa >= 2.0:
  print("You have met at least one of the requirements.")

# Boolean Operators: not

statement_one = False

statement_two = True

credits = 120
gpa = 1.8

if not credits >= 120:
  print("You do not have enough credits to graduate.")
if not gpa >= 2.0:
  print("Your GPA is not high enough to graduate.")
if not credits >= 120 and not gpa >= 2.0:
  print("You do not meet either requirement to graduate!")

# Else statement

credits = 120
gpa = 1.9

if (credits >= 120) and (gpa >= 2.0):
  print("You meet the requirements to graduate!")
else:
  print("You do not meet the requirements to graduate.")

