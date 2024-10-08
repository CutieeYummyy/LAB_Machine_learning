import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, f1_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB, MultinomialNB ,GaussianNB
#Import file CSV
data = pd.read_csv(r"T:\20242025\machinelearning\Data\Education.csv")
print(data.head())
# Tách dữ liệu thành 2 mảng X và y
data["Text"] = data["Text"].str.lower()
X = data["Text"]
X= np.array(X)
y = data["Label"].map({'positive': 1, 'negative': 0})
y = np.array(y)

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vector hóa dữ liệu văn bản thành ma trận đếm
vectorizer = CountVectorizer(binary=True)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Huấn luyện mô hình Bernoulli Naive Bayes
bernoulli_nb = BernoulliNB()
bernoulli_nb.fit(X_train_vec, y_train)
y_pred_bernoulli = bernoulli_nb.predict(X_test_vec)

# Đo lường độ chính xác và F1-score của mô hình Bernoulli Naive Bayes
accuracy_bernoulli = accuracy_score(y_test, y_pred_bernoulli)
f1_bernoulli = f1_score(y_test, y_pred_bernoulli)

# Huấn luyện mô hình Multinomial Naive Bayes
multinomial_nb = MultinomialNB()
multinomial_nb.fit(X_train_vec, y_train)
y_pred_multinomial = multinomial_nb.predict(X_test_vec)

# Đo lường độ chính xác và F1-score của mô hình Multinomial Naive Bayes
accuracy_multinomial = accuracy_score(y_test, y_pred_multinomial)
f1_multinomial = f1_score(y_test, y_pred_multinomial)

# In kết quả
# Tạo DataFrame từ kết quả
results = pd.DataFrame({
    'Model': ['Bernoulli Naive Bayes', 'Multinomial Naive Bayes'],
    'Accuracy': [accuracy_bernoulli, accuracy_multinomial],
    'F1-score': [f1_bernoulli, f1_multinomial]
})

# In bảng kết quả
print(results)