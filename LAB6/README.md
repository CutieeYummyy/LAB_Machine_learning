# LAB 6 Xây dựng hàm Neural Network cơ bản
## Simple neural network
Hàm này cung cấp các công cụ cơ bản để tính toán các mất mát phổ biến và các hàm kích hoạt thường được sử dụng trong mạng neural.
Nó bao gồm các thành phần sau:
-Hàm mất mát:
-- crossEntropyLoss(output, target): Tính toán hàm mất mát Cross-Entropy giữa đầu ra dự đoán (output) và giá trị thực (target).
-- meanSquareError(output, target): Tính toán hàm mất mát Mean Square Error giữa đầu ra dự đoán và giá trị thực.
- Hàm mất mát cho bài toán nhị phân:
-- binaryEntropyLoss(output, target, n): Tính toán hàm mất mát Binary Cross-Entropy cho bài toán nhị phân.
- Các hàm kích hoạt:
-- sigmoid(x): Hàm Sigmoid.
-- relu(x): Hàm ReLU.
-- softmax(zi): Hàm Softmax.
-- tanh(x): Hàm Tanh.
Hàm này có thể được coi là một bộ công cụ cơ bản để xây dựng và huấn luyện mạng neural, bao gồm việc tính toán mất mát và kích hoạt, các yếu tố quan trọng trong quá trình huấn luyện mạng neural.

![image](https://github.com/user-attachments/assets/7e8fcf0b-5cf8-4731-9af2-01ab242a0993)

##  Multi-layer Perceptron
### Các ký hiệu và khái niệm
- Layers
Ngoài Input layers và Output layers, một Multi-layer Perceptron (MLP) có thể có nhiều Hidden layers ở giữa. Các Hidden layers theo thứ tự từ input layer đến output layer được đánh số thứ thự là Hidden layer 1, Hidden layer 2, … 
Một node hình tròn trong một layer được gọi là một unit. Unit ở các input layer, hidden layers, và output layer được lần lượt gọi là input unit, hidden unit, và output unit. Đầu vào của các hidden layer được ký hiệu bởi z, đầu ra của mỗi unit thường được ký hiệu là a (thể hiện activation, tức giá trị của mỗi unit sau khi ta áp dụng activation function lên z ). Đầu ra của unit thứ i  trong layer thứ l  được ký hiệu là a ( l )i. Giả sử thêm rằng số unit trong layer thứ l )  (không tính bias) là d( l). Vector biểu diễn output của layer thứ l  được ký hiệu là a ( l ) ∈ R d ( l) .

![image](https://github.com/user-attachments/assets/05726ff2-8f30-44b1-b6d8-e20fef0debc6) 
![image](https://github.com/user-attachments/assets/dcf9cc04-c43f-4cb3-b0c7-4ec8a1ae2ac3)

### Hàm sigmoid có dạng 
**``Sigmoid`` :**  $$f(s) =  \frac{1}{1 + e^{-s}}$$ với đồ thị như trong Hình 5 (trái). Nếu đầu vào lớn, hàm số sẽ cho đầu ra gần với 1. Với đầu vào nhỏ (rất âm), hàm số sẽ cho đầu ra gần với 0. 
Sigmoid saturate and kill gradients: Một nhược điểm dễ nhận thấy là khi đầu vào có trị tuyệt đối lớn (rất âm hoặc rất dương), gradient của hàm số này sẽ rất gần với 0. Điều này đồng nghĩa với việc các hệ số tương ứng với unit đang xét sẽ gần như không được cập nhật. Bạn đọc sẽ hiểu rõ hơn phần này trong phần Backpropagation. 
Hàm tanh cũng có nhược điểm tương tự về việc gradient rất nhỏ với các đầu vào có trị tuyệt đối lớn.

![Screenshot 2024-11-11 014444](https://github.com/user-attachments/assets/f939bacf-b366-4c78-bec0-3465efafdd6a)

![Screenshot 2024-11-11 014805](https://github.com/user-attachments/assets/b58b8c28-dabd-425c-9dc5-2705bb4a6861)

## Homework

![Screenshot 2024-11-11 004208](https://github.com/user-attachments/assets/dd91075e-f274-4bfe-ae4d-89a670143e7f)
