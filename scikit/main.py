# Install required packages (run once)
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

# 1. Preprocessing function
def preprocess_data(df):
    # Drop unused columns
    df = df.drop(columns=["PassengerId", "Name", "Ticket", "Cabin", "Embarked"])
    
    # Impute missing Age by Pclass median
    age_fill_map = df.groupby("Pclass")["Age"].median().to_dict()
    df["Age"] = df.apply(
        lambda row: age_fill_map[row["Pclass"]] if pd.isnull(row["Age"]) else row["Age"],
        axis=1
    )
    
    # Encode Sex
    df["Sex"] = df["Sex"].map({'male': 1, 'female': 0})
    
    # Feature engineering
    df["FamilySize"] = df["SibSp"] + df["Parch"]
    df["IsAlone"]    = (df["FamilySize"] == 0).astype(int)
    
    # Bin continuous variables
    df["FareBin"] = pd.qcut(df["Fare"], 4, labels=False)
    df["AgeBin"]  = pd.cut(df["Age"], bins=[0, 12, 20, 40, 60, np.inf], labels=False)
    
    return df

# 2. Load and preprocess
data = pd.read_csv("titanic.csv")
data = preprocess_data(data)

# 3. Prepare features and target
X = data.drop(columns=["Survived"])
Y = data["Survived"]

# 4. Train/test split (stratify to keep class balance)
X_train, X_test, y_train, y_test = train_test_split(
    X, Y,
    test_size=0.25,
    random_state=42,
    stratify=Y
)

# 5. Scale features
scaler     = MinMaxScaler()
X_train_sc = scaler.fit_transform(X_train)
X_test_sc  = scaler.transform(X_test)

# 6. Hyperparameter tuning for KNN
def tune_model(X, y):
    param_grid = {
        "n_neighbors": range(1, 21),
        "metric":      ["euclidean", "manhattan", "minkowski"],
        "weights":     ["uniform", "distance"]
    }
    knn = KNeighborsClassifier()
    grid = GridSearchCV(knn, param_grid, cv=5, n_jobs=-1)
    grid.fit(X, y)
    return grid.best_estimator_

best_model = tune_model(X_train_sc, y_train)

# 7. Evaluation
def evaluate_model(model, X, y):
    preds = model.predict(X)
    acc   = accuracy_score(y, preds)
    cm    = confusion_matrix(y, preds)
    return acc, cm

accuracy, cmatrix = evaluate_model(best_model, X_test_sc, y_test)
print(f"Accuracy: {accuracy*100:.2f}%")
print("Confusion Matrix:\n", cmatrix)

# 8. Plot confusion matrix
def plot_model(matrix):
    plt.figure(figsize=(8, 6))
    sns.heatmap(
        matrix,
        annot=True, fmt="d",
        xticklabels=["Not Survived", "Survived"],
        yticklabels=["Not Survived", "Survived"]
    )
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

plot_model(cmatrix)
