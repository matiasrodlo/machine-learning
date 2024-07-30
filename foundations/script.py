libraries = ["NumPy", "SciPy", "Pandas", "Matplotlib", "Seaborn"]
completion = [100, 100, 96, 0, 0]

libraries.append("scikit-learn")
completion.append(0)

gradebook = list(zip(libraries, completion))

print("Lesson Completion Rates:")
print(gradebook)
print("\n")

# What's next?

# gradebook.append(("BeautifulSoup", 0))
# gradebook.append(("Tensorflow", 0))

# Analyzing Data with Pandas
import codecademylib3_seaborn

# Paste code here:
import pandas as pd

# Load data
df = pd.read_csv('page_visits.csv')

# Display data
print(df.head())

# Visualizing Data with Matplotlib and Seaborn
import codecademylib3_seaborn
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

hour = range(24)

viewers_hour = [30, 17, 34, 29, 19, 14, 3, 2, 4, 9, 5, 48, 62, 58, 40, 51, 69, 55, 76, 81, 102, 120, 71, 63]

plt.title("Codecademy Learners Time Series")

plt.xlabel("Hour")
plt.ylabel("Viewers")

plt.plot(hour, viewers_hour)

plt.legend(['2015-01-01'])

ax = plt.subplot()

ax.set_facecolor('seashell')

ax.set_xticks(hour)
ax.set_yticks([0, 20, 40, 60, 80, 100, 120])

y_upper = [i + (i*0.15) for i in viewers_hour]
y_lower = [i - (i*0.15) for i in viewers_hour]

plt.fill_between(hour, y_lower, y_upper, alpha=0.2)

# Add the code here:
plt.show()

# Probability

from simulate import simulate

num_people_in_room = 100 			#Change This Number (keep it smaller than 100 to save processing power)

simulate(num_people_in_room) 