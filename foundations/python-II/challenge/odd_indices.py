#Write your function here
def odd_indices(my_list):
  new_list = []
  for i in range(len(my_list)):  # Go through every index in the list
    if i % 2 != 0:               # If the index is odd (1, 3, 5...)
      new_list.append(my_list[i])  # Add the element at that index
  return new_list

#Uncomment the line below when your function is done
#print(odd_indices([4, 3, 7, 10, 11, -2]))