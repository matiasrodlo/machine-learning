# Install
# pip3 install pandas numpy scikit-learn matplotlib seaborn

# Imports
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

import matplotlib.pyplot as plt
import seaborn as sns

# Data cleaning and feature engineering

data = pd.read_csv("titanic.csv")
data.info()