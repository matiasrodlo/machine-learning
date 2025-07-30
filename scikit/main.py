# Install required packages (run once in your terminal):
# pip3 install pandas numpy scikit-learn matplotlib seaborn

# 1) IMPORT LIBRARIES
import pandas as pd            # 🔹 pandas is for handling tables (like Excel sheets) in Python
import numpy as np             # 🔹 numpy helps with math on arrays of numbers

from sklearn.model_selection import train_test_split, GridSearchCV  
# 🔹 train_test_split: splits data into "teach" vs. "test" sets  
# 🔹 GridSearchCV: tries many settings to find the best model automatically

from sklearn.preprocessing import MinMaxScaler  
# 🔹 MinMaxScaler: squishes all numbers into the 0–1 range so they're comparable

from sklearn.neighbors import KNeighborsClassifier  
# 🔹 KNeighborsClassifier: the K‑Nearest Neighbors algorithm (simple: vote among closest “neighbors”)

from sklearn.metrics import accuracy_score, confusion_matrix  
# 🔹 accuracy_score: percentage of correct guesses  
# 🔹 confusion_matrix: detailed table of right/wrong predictions

import matplotlib.pyplot as plt  
import seaborn as sns  
# 🔹 matplotlib + seaborn: drawing charts (we’ll plot our confusion matrix)


# 2) DATA CLEANING & FEATURE ENGINEERING FUNCTION
def preprocess_data(df):
    """
    Takes raw Titanic data and:
      - removes useless columns
      - fills missing ages
      - encodes text into numbers
      - creates new helpful features
      - buckets continuous numbers into categories
    """
    # a) DROP COLUMNS we won't use
    df = df.drop(columns=[
        "PassengerId",  # just an ID, not predictive
        "Name",         # name text isn’t useful for KNN
        "Ticket",       # complicated text, skip it
        "Cabin",        # mostly missing values, skip
        "Embarked"      # port of boarding—drop for simplicity
    ])

    # b) FILL missing ages by using the median age of each Pclass
    age_fill_map = df.groupby("Pclass")["Age"].median().to_dict()
    # 🔹 groupby("Pclass") finds median age per class → map of {1: 37, 2: 29, 3: 24} for example
    df["Age"] = df.apply(
        lambda row: age_fill_map[row["Pclass"]]
        if pd.isnull(row["Age"])   # if Age is missing
        else row["Age"],           # otherwise keep original
        axis=1
    )

    # c) ENCODE Sex as numbers: male→1, female→0
    df["Sex"] = df["Sex"].map({'male': 1, 'female': 0})

    # d) NEW FEATURES
    df["FamilySize"] = df["SibSp"] + df["Parch"]
    # 🔹 SibSp = siblings/spouses aboard; Parch = parents/children aboard
    df["IsAlone"] = (df["FamilySize"] == 0).astype(int)
    # 🔹 1 if no family members, 0 otherwise

    # e) BINNING continuous variables into ordinal categories
    df["FareBin"] = pd.qcut(df["Fare"], 4, labels=False)
    # 🔹 qcut splits Fare into 4 equal‑sized groups (0,1,2,3)
    df["AgeBin"]  = pd.cut(
        df["Age"],
        bins=[0, 12, 20, 40, 60, np.inf],
        labels=False
    )
    # 🔹 cut by fixed age ranges: child, teen, adult, middle-age, senior

    return df  # return the cleaned & feature‑engineered DataFrame


# 3) LOAD & PREPROCESS DATA
data = pd.read_csv("titanic.csv")  # 📥 read the CSV file into a table
data = preprocess_data(data)        # 🧹 clean & add new columns


# 4) SPLIT FEATURES & TARGET
X = data.drop(columns=["Survived"])  # 🚀 X is what model sees (all columns except Survived)
Y = data["Survived"]                 # 🎯 Y is what we want to predict


# 5) TRAIN/TEST SPLIT
X_train, X_test, y_train, y_test = train_test_split(
    X, Y,
    test_size=0.25,     # 25% of data reserved for testing later
    random_state=42,    # ensures you get the same split each run
    stratify=Y          # keeps the same survive/die ratio in both sets
)


# 6) SCALE FEATURES TO 0–1
scaler = MinMaxScaler()
X_train_sc = scaler.fit_transform(X_train)  # learn min/max on train set
X_test_sc  = scaler.transform(X_test)       # apply that same scaling to test set


# 7) HYPERPARAMETER TUNING FOR KNN
def tune_model(X, y):
    """
    Tries K from 1 to 20, three distance metrics, and two weighting schemes.
    Picks the combination with highest cross‑validation accuracy.
    """
    param_grid = {
        "n_neighbors": range(1, 21),              # try 1 through 20 neighbors
        "metric":      ["euclidean", "manhattan", "minkowski"],
        "weights":     ["uniform", "distance"]     # uniform = equal vote; distance = closer neighbors count more
    }
    knn = KNeighborsClassifier()                  # create base KNN model
    grid = GridSearchCV(knn, param_grid, cv=5, n_jobs=-1)
    grid.fit(X, y)                                # test all combos via 5‑fold cross‑validation
    return grid.best_estimator_                   # return the best‑found model

best_model = tune_model(X_train_sc, y_train)  # 🔍 find the best KNN settings on training data


# 8) EVALUATION ON TEST SET
def evaluate_model(model, X, y):
    preds = model.predict(X)                   # model’s guesses
    acc   = accuracy_score(y, preds)           # percent correct
    cm    = confusion_matrix(y, preds)         # table of yes/no vs. predicted yes/no
    return acc, cm

accuracy, cmatrix = evaluate_model(best_model, X_test_sc, y_test)
print(f"Accuracy: {accuracy*100:.2f}%")         # e.g. "Accuracy: 82.34%"
print("Confusion Matrix:\n", cmatrix)           # printed 2×2 array


# 9) PLOT CONFUSION MATRIX
def plot_model(matrix):
    plt.figure(figsize=(8, 6))
    sns.heatmap(
        matrix,
        annot=True, fmt="d",                    # annotate with integer counts
        xticklabels=["Not Survived", "Survived"],
        yticklabels=["Not Survived", "Survived"]
    )
    plt.title("Confusion Matrix")               # chart title
    plt.xlabel("Predicted Label")               # x‑axis label
    plt.ylabel("True Label")                    # y‑axis label
    plt.show()                                  # display the plot

plot_model(cmatrix)  # draw the heatmap
