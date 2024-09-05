# String 
favorite_word = "legenden"
print(favorite_word)

# Index string 

my_name = "Matias Rodlo"
first_initial = my_name[0]

# Slicing string 

first_name = "Rodrigo"
last_name = "Villanueva"

new_account = last_name[:5]
temp_password = last_name[2:6]

# Concatenating strings

first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name, last_name):
  account_name = first_name[:3] + last_name[:3]
  return account_name

new_account = account_generator(first_name, last_name)

print(new_account)

# More and More String Slicing

first_name = "Reiko"
last_name = "Matsuki"
first_length = len(first_name)
last_length = len(last_name)

def password_generator(first_name, last_name):
  return first_name[first_length-3:] + last_name[last_length-3:]

temp_password = password_generator(first_name, last_name) 