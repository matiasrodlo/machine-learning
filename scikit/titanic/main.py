# 1) SETUP: Install required packages (run this once in your terminal)
# ---------------------------------------------------------------
# pip3 install pandas numpy scikit-learn matplotlib seaborn

# 2) IMPORT LIBRARIES
# ---------------------------------------------------------------
import pandas as pd             # 📊 For working with tabular data (like Excel)
import numpy as np              # 🔢 For numerical operations (arrays, math)

from sklearn.model_selection import train_test_split, GridSearchCV  
# - train_test_split: to split data into training and test sets  
# - GridSearchCV: to search for the best hyperparameters automatically

from sklearn.preprocessing import MinMaxScaler  
# - MinMaxScaler: scales features to a 0–1 range

from sklearn.neighbors import KNeighborsClassifier  
# - KNN algorithm: predicts based on “k” nearest data points

from sklearn.metrics import accuracy_score, confusion_matrix  
# - accuracy_score: computes percentage correct  
# - confusion_matrix: shows true vs. predicted breakdown

import matplotlib.pyplot as plt  # 📈 For creating plots
import seaborn as sns            # 🎨 For prettier statistical plots

# 3) DATA LOADING & INITIAL INSPECTION
# ---------------------------------------------------------------
data = pd.read_csv("titanic.csv")          # Load CSV into a DataFrame
data.info()                                # Show data types + non-null counts
print(data.isnull().sum())                 # Show how many missing values per column

# 4) PREPROCESSING FUNCTIONS
# ---------------------------------------------------------------

def fill_missing_ages(df):
    """
    🔧 Fill missing Age values based on the median Age of each passenger class (Pclass).
    """
    # Compute median Age per Pclass
    median_by_class = df.groupby("Pclass")["Age"].median().to_dict()
    # Replace missing Age with that class's median
    df["Age"] = df.apply(
        lambda row: median_by_class[row["Pclass"]] 
                    if pd.isnull(row["Age"]) 
                    else row["Age"],
        axis=1
    )

def preprocess_data(df):
    """
    🧹 Clean data, engineer features, and prepare for modeling.
    """
    # 4.1) Drop columns we won’t use
    df.drop(columns=["PassengerId", "Name", "Ticket", "Cabin"], inplace=True)

    # 4.2) Handle Embarked: fill missing with most common 'S', then drop
    df["Embarked"].fillna("S", inplace=True)
    df.drop(columns=["Embarked"], inplace=True)

    # 4.3) Fill missing Age values
    fill_missing_ages(df)

    # 4.4) Convert Sex to numeric: male → 1, female → 0
    df["Sex"] = df["Sex"].map({'male': 1, 'female': 0})

    # 4.5) Create new features:
    #   • FamilySize = SibSp + Parch (total relatives aboard)
    #   • IsAlone = 1 if FamilySize == 0 else 0
    df["FamilySize"] = df["SibSp"] + df["Parch"]
    df["IsAlone"]    = np.where(df["FamilySize"] == 0, 1, 0)

    # 4.6) Bin continuous variables into categories:
    #   • FareBin: quartiles of Fare
    #   • AgeBin: age groups [0-12, 13-20, 21-40, 41-60, 61+]
    df["FareBin"] = pd.qcut(df["Fare"], 4, labels=False)
    df["AgeBin"]  = pd.cut(
        df["Age"],
        bins=[0,12,20,40,60,np.inf],
        labels=False
    )

    return df

# 5) APPLY PREPROCESSING & SPLIT DATA
# ---------------------------------------------------------------
data = preprocess_data(data)                    # Cleaned + feature‑engineered
X = data.drop(columns=["Survived"])              # Features for training
y = data["Survived"]                             # Target variable

# Split into 75% train / 25% test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# 6) SCALE FEATURES
# ---------------------------------------------------------------
scaler    = MinMaxScaler()                      
X_train   = scaler.fit_transform(X_train)       # Learn & apply scaling on train
X_test    = scaler.transform(X_test)            # Apply same scaling on test

# 7) HYPERPARAMETER TUNING WITH GRID SEARCH
# ---------------------------------------------------------------
def tune_model(X_train, y_train):
    """
    🔍 Try different KNN settings to find the best one.
    """
    param_grid = {
        "n_neighbors": range(1, 21),                     # k = 1 to 20
        "metric": ["euclidean", "manhattan", "minkowski"],  
        "weights": ["uniform", "distance"]
    }
    knn = KNeighborsClassifier()
    grid_search = GridSearchCV(
        knn, param_grid, cv=5, n_jobs=-1, verbose=1  # cv=5 folds, parallel jobs, show progress
    )
    grid_search.fit(X_train, y_train)              # Run the search
    return grid_search.best_estimator_             # Return best model

best_model = tune_model(X_train, y_train)         # Execute tuning

# 8) EVALUATE THE BEST MODEL
# ---------------------------------------------------------------
def evaluate_model(model, X_test, y_test):
    """
    📊 Compute accuracy and confusion matrix on test data.
    """
    preds    = model.predict(X_test)               
    acc      = accuracy_score(y_test, preds)       # % correct
    matrix   = confusion_matrix(y_test, preds)     # 2×2 breakdown
    return acc, matrix

accuracy, matrix = evaluate_model(best_model, X_test, y_test)

print(f"Accuracy: {accuracy*100:.2f}%")
print("Confusion Matrix:")
print(matrix)

# 9) VISUALIZE CONFUSION MATRIX
# ---------------------------------------------------------------
def plot_model(matrix):
    """
    🖼️ Display a heatmap of the confusion matrix.
    """
    plt.figure(figsize=(8,6))
    sns.heatmap(
        matrix,
        annot=True, fmt="d",
        xticklabels=["Pred: Not Survived", "Pred: Survived"],
        yticklabels=["True: Not Survived", "True: Survived"]
    )
    plt.title("Titanic KNN Confusion Matrix")
    plt.xlabel("Predicted Label")
    plt.ylabel("True Label")
    plt.show()

plot_model(matrix)
