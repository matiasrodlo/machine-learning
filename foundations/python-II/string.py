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

# Negative Indices

company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

second_to_last = company_motto[-2]

final_word = company_motto[-4:]

#  Strings are Immutable

first_name = "Bob"
last_name = "Daily"

fixed_first_name = "R" + first_name[1:]

# Escape Characters

password = "theycallme\"crazy\"91"

# Iterating through Strings

def get_length(word):
  counter = 0
  for letter in word:
    counter += 1
  return counter

# Strings and Conditionals (Part One)

def letter_check(word, letter):
  for character in word:
    if character == letter:
      return True
  return False

# Strings and Conditionals (Part Two)

def contains(big_string, little_string):
  return little_string in big_string

def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  return common

# Review

def username_generator(first_name, last_name):
    if len(first_name) < 3:
        user_name = first_name
    else:
        user_name = first_name[0:3]
    if len(last_name) < 4:
        user_name += last_name
    else:
        user_name += last_name[0:4]
    return user_name
  
    
def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i-1]
    return password

# Formatting method
poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()
print(poem_title)
print(poem_title_fixed)

poem_author_fixed = poem_author.upper()
print(poem_author)
print(poem_author_fixed)

# Split String

line_one = "The sky has given over"

line_one_words = line_one.split()

# Split String II

authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(',')

print(author_names)

author_last_names = []
for name in author_names:
  author_last_names.append(name.split()[-1])
  
print(author_last_names)

# Splitting Strings III

spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split('\n')