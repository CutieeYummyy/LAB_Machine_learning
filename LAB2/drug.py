import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, f1_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB, MultinomialNB, GaussianNB
#import file CSV
data = pd.read_csv(r"T:\20242025\machinelearning\Data\drug200.csv")
print(data.head())
# Chuyển cột "Drug" của dữ liệu thành X
y = data[["Drug"]]
# Đảm bảo rằng việc chuyển đổi giá trị của cột "BP" và "Cholesterol" thành số được thực hiện đúng
b= data["BP"].map({'NORMAL': 1, 'LOW': 0, 'HIGH': 2})
a=data['Cholesterol'].map({'NORMAL': 1, 'HIGH': 0})
X= np.column_stack((b, a))
# Chia tập dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Initialize the Gaussian Naive Bayes model
gnb = GaussianNB()

# Train the model on the training data
gnb.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = gnb.predict(X_test)

# Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

# Output the results
print(f"Accuracy: {accuracy * 100:.2f}%")
print("\nClassification Report:\n", report)