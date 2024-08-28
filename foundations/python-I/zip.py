owners = ["Jenny", "Alexus", "Sam", "Grace"]
dogs_names = ["Elphonse", "Dr. Doggy DDS", "Carter", "Ralph"]

# Step 1: Use zip() to combine the lists
names_and_dogs_names = zip(owners, dogs_names)

# Step 2: Convert the zip object to a list
list_of_names_and_dogs_names = list(names_and_dogs_names)

# Step 3: Print the resulting list
print(list_of_names_and_dogs_names)