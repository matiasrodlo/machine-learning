# Write your function here
def append_size(my_list):
  element = len(my_list)
  my_list.append(element) 
  return my_list

# Uncomment the line below when your function is done
print(append_size([23, 42, 108]))