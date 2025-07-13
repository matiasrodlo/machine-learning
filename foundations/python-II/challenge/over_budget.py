# Monthly budget
budget = 2000

# Monthly expenses
food_bill = 200
electricity_bill = 100
internet_bill = 60
rent = 1500

# Calculate the total amount of expenses
total = food_bill + electricity_bill + internet_bill + rent

# Check if the total is greater than the budget and store the result in over_budget
over_budget = None

def budget_checker(budget, total):
  global over_budget
  if (budget >= total):
    over_budget = False
  else:
    over_budget = True

# Uncomment the below lines to see the results

budget_checker(budget, total)

print("Total: " + str(total))
print("Is it over budget? " + str(over_budget))
