# LAB 2 Phân phối Bernoulli và Multinomial
Naive Bayes là một kỹ thuật đơn giản để xây dựng các bộ phân loại: các mô hình gán nhãn lớp cho các trường hợp vấn đề, được biểu diễn dưới dạng các vectơ giá trị đặc điểm , trong đó các nhãn lớp được rút ra từ một số tập hữu hạn.

![image](https://github.com/user-attachments/assets/bf0edc02-fffb-4248-b938-30f4642e7be6)


Khi xử lý dữ liệu liên tục, một giả định điển hình là các giá trị liên tục liên quan đến mỗi lớp được phân phối theo phân phối chuẩn (hoặc Gaussian)

![image](https://github.com/user-attachments/assets/1c91ec4a-311a-4f21-ab1b-d4952d76ec5f)

Bài toán sử dụng Naive Bayes dự đoán cảm xúc của văn bản là tích cực hay tiêu cực và so sánh kết quả của hai phân phối đó với các tham số 
**``Accuracy`` :**  $$Accuracy = \frac{(TP + TN)}{All}$$


\
**``Precision`` :**   $$Precision = \frac{TP}{(TP + FP)}$$


\
**``Recall`` :**   $$Recall = \frac{TP}{(TP + FN)}$$


\
**``F1-score`` :**    $F_{1}-score = 2 \cdot \frac{Precision \cdot Recall}{Precision + Recall} = \frac{TP}{TP + \frac{FN + FP}{2}}$$
#Sử dụng mô hình Bernoulli với tập dữ liệu Education
BernoulliNB là một biến thể của Naive Bayes sử dụng với các đặc trưng dữ liệu nhị phân (binary features). Mô hình này giả định rằng các đặc trưng là độc lập và mỗi đặc trưng có xác suất là 0 hoặc 1.
Thuật toán Bernoulli Naive Bayes ước lượng xác suất của mỗi từ (đặc trưng) xuất hiện trong các tài liệu thuộc một lớp cụ thể (positive hoặc negative). Sau đó, nó sẽ sử dụng luật Bayes để tính toán xác suất hậu nghiệm cho từng lớp và chọn lớp có xác suất cao nhất làm kết quả dự đoán.

![Screenshot 2024-10-11 002035](https://github.com/user-attachments/assets/8dd64108-a491-4e43-8fc4-50b77a71963e)
![Screenshot 2024-10-11 002053](https://github.com/user-attachments/assets/8c226a3a-9fa6-45b7-9ebf-6db998572762)

# Sử dụng mô hình Naive Bayes cho tập dữ liệu Drug200
Đây là một thuật toán dựa trên lý thuyết Bayes với giả định các đặc trưng tuân theo phân phối chuẩn (Gaussian distribution).
Gaussian Naive Bayes sử dụng công thức Bayes để tính xác suất hậu nghiệm cho từng lớp (ở đây là các loại thuốc) dựa trên các đặc trưng như giới tính, huyết áp, và cholesterol. Sau đó, mô hình sẽ chọn lớp có xác suất cao nhất làm kết quả dự đoán.

![image](https://github.com/user-attachments/assets/bb4f5e9a-7368-46db-91de-22e976bb03b3)




