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


![image](https://github.com/user-attachments/assets/05726ff2-8f30-44b1-b6d8-e20fef0debc6) 

### Hàm sigmoid có dạng 
# Giới Thiệu về MLP (Multi-Layer Perceptron)

Mạng Perceptron Đa lớp (MLP) là một loại mô hình học sâu thuộc vào nhóm mạng nơ-ron, được sử dụng rộng rãi trong các bài toán phân loại và hồi quy. MLP bao gồm nhiều lớp nơ-ron (neuron) kết nối đầy đủ với nhau: một lớp đầu vào, một hoặc nhiều lớp ẩn và một lớp đầu ra. Mỗi nơ-ron trong lớp ẩn và lớp đầu ra hoạt động bằng cách áp dụng một hàm kích hoạt (activation function) cho tổng trọng số của các đầu vào.

## Cấu Trúc Cơ Bản của MLP

1. **Lớp Đầu Vào**: Nhận dữ liệu đầu vào.
2. **Lớp Ẩn**: Thực hiện xử lý thông tin qua các nơ-ron với trọng số và hàm kích hoạt.
3. **Lớp Đầu Ra**: Cung cấp dự đoán cuối cùng cho đầu vào.

![image](https://github.com/user-attachments/assets/dcf9cc04-c43f-4cb3-b0c7-4ec8a1ae2ac3)
### Công Thức

1. **Xác định trọng số**: Trong một MLP, mỗi nơ-ron trong lớp ẩn nhận đầu vào từ lớp trước và thực hiện tính toán như sau:

   $$z = W \cdot x + b$$

   - $$z$$: Đầu ra chưa kích hoạt của nơ-ron.
   - $$W$$: Trọng số (weight) của nơ-ron.
   - $x$: Đầu vào từ lớp trước.
   - $b$: Hệ số lệch (bias).

3. **Hàm Kích Hoạt**: Để tính toán đầu ra của một nơ-ron, hàm kích hoạt như hàm sigmoid, ReLU (Rectified Linear Unit), hoặc tanh thường được sử dụng:

   - **Sigmoid**:
     $$a = \frac{1}{1 + e^{-z}}$$

   - **ReLU**:
     $$a = \max(0, z)$$

   - **Tanh**:
     $$a = \frac{e^{z} - e^{-z}}{e^{z} + e^{-z}}$$

   - Trong đó, $a$ là đầu ra của nơ-ron sau khi áp dụng hàm kích hoạt.

4. **Lớp Đầu Ra**: Đầu ra của MLP được tính giống như lớp ẩn nhưng không áp dụng hàm kích hoạt (hoặc sử dụng hàm kích hoạt phù hợp cho bài toán phân loại):

   $$\hat{y} = \text{softmax}(z) \quad \text{(cho phân loại nhiều lớp)}$$

5. **Sai số và Tối ưu**: Sai số giữa dự đoán và giá trị thực tế được tính toán và sử dụng để cập nhật trọng số thông qua phương pháp lan truyền ngược (backpropagation):

   $$L = -\sum_{i} y_i \log(\hat{y_i})$$

   - $L$ là hàm mất mát (loss function).
   - $y_i$ là nhãn thực tế.
   - $\hat{y_i}$ là dự đoán của mô hình.

## Kết Luận

Mạng Perceptron Đa lớp là một trong những kiến trúc nền tảng của học sâu, giúp mô hình hóa các quan hệ phức tạp trong dữ liệu và đã được chứng minh là hiệu quả trong nhiều bài toán thực tế.


![Screenshot 2024-11-11 014444](https://github.com/user-attachments/assets/f939bacf-b366-4c78-bec0-3465efafdd6a)

![Screenshot 2024-11-11 014805](https://github.com/user-attachments/assets/b58b8c28-dabd-425c-9dc5-2705bb4a6861)

## Homework

![Screenshot 2024-11-11 004208](https://github.com/user-attachments/assets/dd91075e-f274-4bfe-ae4d-89a670143e7f)
