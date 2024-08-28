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