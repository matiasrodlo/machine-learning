# Adding by Index: Insert

front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
print(front_display_list)

front_display_list.insert(0, "Pineapple")

# Removing by Index: Pop

data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
print(data_science_topics)

# Your code below: 

data_science_topics.pop()
print(data_science_topics)

data_science_topics.pop(3)
print(data_science_topics)

# List Range: 
number_list = range(0,9)
print(list(number_list))

zero_to_seven = range(0,8)
print(list(zero_to_seven))

# Range with skip: 

range_five_three = range(5, 15, 3)
range_diff_five = range(0, 40, 5)

# Length: 

long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]

big_range = range(2, 3000, 100)

long_list_len = len(long_list)
print(long_list_len)
print(long_list_len)

big_range_length = len(big_range)
print(big_range_length)

# Slice a list: 

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

beginning = suitcase[0:2]

print(beginning)
middle = suitcase[2:4]

# Slice a list II: 

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

last_two_elements = suitcase[-2:]
print(last_two_elements)

slice_off_last_three = suitcase[:-3]
print(slice_off_last_three)

# Counting in a list: 

votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

jake_votes = votes.count("Jake")
print(jake_votes)

# Sorting list I
addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]

names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
names.sort()
addresses.sort()
print(addresses)

cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
sorted_cities = cities.sort(reverse=True)
print(sorted_cities)

# Sorting list II

games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]

games_sorted = sorted(games)
print(games)
print(games_sorted)

# Review

inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

inventory_len = len(inventory)
first = inventory[0]
last = inventory[-1]
inventory_2_6 = inventory[2:6]
first_3 = inventory[:3]
twin_beds = inventory.count("twin bed")
removed_item = inventory.pop(4)
inventory.insert(10, "19th Century Bed Frame")
print(inventory.sort())