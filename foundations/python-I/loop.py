# Write 10 print() statements below! 
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")

# For loop induction

board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]

sport_games = ["football", "hockey", "baseball", "cricket"]

for game in board_games:
  print(game)

for sports in sport_games:
  print(sports)

# Loop using range

promise = "I will finish the python loops module!"

for temp in range(5):
  print(promise)

  # While Loop
count = 0
print("Starting While Loop")
while count <= 3:
  # Loop Body
  # Print if the condition is still true
  print("Loop Iteration - count <= 3 is still true")
  # Print the current value of count 
  print("Count is currently " + str(count))
  # Increment count
  count += 1
  print(" ----- ")
print("While Loop ended")

# Your code below: 
countdown = 10
while countdown >= 0:
  print(countdown)
  countdown -= 1
print("We have liftoff!")

# While Loops: Lists: 

python_topics = ["variables", "control flow", "loops", "modules", "classes"]

length = len(python_topics)
index = 0
while index < length:
  print("I am learning about " + python_topics[index])
  index += 1

# Infinity Loop

students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
  print(student)

# Loop Control: Break

  dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed == dog_breed_I_want:
    print("They have the dog I want!") 
    break

# Loop Control: Continue

  ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for i in ages:
  if i < 21:
    continue
  print(i)

# Nested Loops

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0;

for location in sales_data:
  print(location)
  for elements in location:
    scoops_sold += elements

print(scoops_sold)

# List comprehension

grades = [90, 88, 62, 76, 74, 89, 48, 57]

scaled_grades = [grade + 10 for grade in grades]
print(scaled_grades)