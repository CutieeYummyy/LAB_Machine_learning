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
