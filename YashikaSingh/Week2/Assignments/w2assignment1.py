import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# PART A: DATASET UNDERSTANDING

# Q1 Load dataset
df = pd.read_csv("Dataset 2 (1).csv")

print("First 5 Records:")
print(df.head())

# Q2 Number of rows and columns
print("\nShape of Dataset:")
print(df.shape)

# Q3 Column names
print("\nColumn Names:")
print(df.columns)

# Q4 Numerical and categorical features
print("\nNumerical Features:")
print(df.select_dtypes(include=np.number).columns)

print("\nCategorical Features:")
print(df.select_dtypes(include='object').columns)

# Q5 Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# PART B: EXPLORATORY DATA ANALYSIS

# Q6 Average age
print("\nAverage Age:")
print(df["Age"].mean())

# Q7 Average watch hours
print("\nAverage Watch Hours Per Week:")
print(df["WatchHoursPerWeek"].mean())

# Q8 Average monthly spend
print("\nAverage Monthly Spending:")
print(df["MonthlySpend"].mean())

# Q9 Subscription category counts
print("\nSubscription Counts:")
print(df["SubscriptionType"].value_counts())

# Q10 Renewal percentage
renewal_percentage = (
    (df["SubscriptionRenewed"] == "Yes").mean()
) * 100

print("\nSubscription Renewal Percentage:")
print(renewal_percentage)

# PART C: DATA PREPARATION

# Q11 Convert categorical features into numerical form
df_encoded = df.copy()

label_encoders = {}

categorical_cols = [
    "Gender",
    "SubscriptionType",
    "FavoriteGenre",
    "SubscriptionRenewed"
]

for col in categorical_cols:
    le = LabelEncoder()
    df_encoded[col] = le.fit_transform(df_encoded[col])
    label_encoders[col] = le

print("\nEncoded Dataset:")
print(df_encoded.head())

# Q12 Define X and y
X = df_encoded.drop(
    columns=["UserID", "SubscriptionRenewed"]
)

y = df_encoded["SubscriptionRenewed"]

# Q13 Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# PART D: DECISION TREE

# Q14 Train Decision Tree
dt_model = DecisionTreeClassifier(
    random_state=42
)

dt_model.fit(X_train, y_train)

# Q15 Accuracy
dt_pred = dt_model.predict(X_test)

dt_accuracy = accuracy_score(
    y_test,
    dt_pred
)

print("\nDecision Tree Accuracy:")
print(dt_accuracy)

# Q16 Confusion Matrix
cm = confusion_matrix(
    y_test,
    dt_pred
)

print("\nDecision Tree Confusion Matrix:")
print(cm)

# Feature Importance
importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": dt_model.feature_importances_
})

print("\nFeature Importance:")
print(
    importance.sort_values(
        by="Importance",
        ascending=False
    )
)

# PART E: KNN
 
# Q17 Train KNN
knn_model = KNeighborsClassifier(
    n_neighbors=5
)

knn_model.fit(X_train, y_train)

knn_pred = knn_model.predict(X_test)

# Q18 Compare Accuracy
knn_accuracy = accuracy_score(
    y_test,
    knn_pred
)

print("\nKNN Accuracy:")
print(knn_accuracy)

print("\nComparison:")
print("Decision Tree =", dt_accuracy)
print("KNN =", knn_accuracy)

if knn_accuracy > dt_accuracy:
    print("KNN performed better.")
else:
    print("Decision Tree performed better.")

# PART F: LINEAR REGRESSION

# Q19 Predict Monthly Spending

X_reg = df_encoded.drop(
    columns=["UserID", "MonthlySpend"]
)

y_reg = df_encoded["MonthlySpend"]

X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(
    X_reg,
    y_reg,
    test_size=0.20,
    random_state=42
)

lr_model = LinearRegression()

lr_model.fit(
    X_train_reg,
    y_train_reg
)

# Q20 Predict Monthly Spending for New User

new_user = pd.DataFrame({
    "Age": [25],
    "Gender": [1],
    "SubscriptionType": [2],
    "WatchHoursPerWeek": [15],
    "DevicesUsed": [3],
    "FavoriteGenre": [0],
    "AdClicks": [10],
    "SubscriptionRenewed": [1]
})

predicted_spend = lr_model.predict(new_user)

print("\nPredicted Monthly Spend:")
print(predicted_spend[0])