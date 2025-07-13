# Write your function here
def append_sum(my_list):
  count = 1
  while count <= 3:
    sum = my_list[-1] + my_list[-2]
    my_list.append(sum)
    count += 1
  return my_list

# Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))