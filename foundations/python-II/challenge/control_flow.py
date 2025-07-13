num1 = 6
num2 = 3
not_ten = None

# Write your if statement here
def num(num1, num2):
  global not_ten  # This tells Python to use the variable outside the function
  if (num1 + num2 != 10):
    not_ten = True
  else:
    not_ten = False

num(num1, num2)  # 🔹 You MUST call the function here

print("Is the sum of the numbers not equal to 10? " + str(not_ten))
