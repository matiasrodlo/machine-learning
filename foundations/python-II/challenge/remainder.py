# Write your remainder function here:

def remainder(num1, num2):
  twice = num1 * 2
  half = num2 / 2
  return twice % half

# Uncomment these function calls to test your remainder function:
print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0