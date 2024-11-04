# LAB 5 : Support Vector Machine (SVM)
SVM là một thuật toán giám sát, nó có thể sử dụng cho cả việc phân loại hoặc đệ quy. Tuy nhiên nó được sử dụng chủ yếu cho việc phân loại,đồ thị dữ liệu là các điểm trong n chiều ( ở đây n là số lượng các tính năng bạn có) với giá trị của mỗi tính năng sẽ là một phần liên kết. Sau đó thực hiện tìm "đường bay" (hyper-plane) phân chia các lớp. Hyper-plane nó chỉ hiểu đơn giản là 1 đường thẳng có thể phân chia các lớp ra thành hai phần riêng biệt.

![image](https://github.com/user-attachments/assets/2ec2844f-d79a-4b5a-a925-cb4e4fa45d15)

Support Vectors hiểu một cách đơn giản là các đối tượng trên đồ thị tọa độ quan sát, Support Vector Machine là một biên giới để chia hai lớp tốt nhất.
### Ưu điểm của máy vectơ hỗ trợ là:
- Có hiệu quả trong không gian có nhiều chiều.
- Vẫn hiệu quả trong trường hợp số chiều lớn hơn số mẫu.
- Sử dụng một tập hợp con các điểm đào tạo trong hàm quyết định (gọi là vectơ hỗ trợ), do đó cũng tiết kiệm bộ nhớ.
- Đa năng: có thể chỉ định các hàm Kernel khác nhau cho hàm quyết định. Các kernel phổ biến được cung cấp, nhưng cũng có thể chỉ định các kernel tùy chỉnh.
### Những nhược điểm của máy vectơ hỗ trợ bao gồm:
Nếu số lượng tính năng lớn hơn nhiều so với số lượng mẫu, hãy tránh việc lựa chọn hàm Kernel quá mức và thuật ngữ chính quy hóa là rất quan trọng.
SVM không trực tiếp cung cấp ước tính xác suất, chúng được tính toán bằng cách sử dụng phương pháp xác thực chéo năm lần tốn kém (xem Điểm và xác suất bên dưới).
Các máy vectơ hỗ trợ trong scikit-learn hỗ trợ cả vectơ mẫu dày đặc ( numpy.ndarrayvà có thể chuyển đổi sang vectơ đó bằng numpy.asarray) và thưa thớt (bất kỳ scipy.sparse) làm đầu vào. Tuy nhiên, để sử dụng SVM để đưa ra dự đoán cho dữ liệu thưa thớt, nó phải phù hợp với dữ liệu đó.
### Ví dụ về thuật toán
-- Bài 1 :
![Screenshot 2024-11-04 125310](https://github.com/user-attachments/assets/ec2af5ec-ff96-4340-bf97-e89de8463786)

-- Bài 2: 
![image](https://github.com/user-attachments/assets/4db23d7a-07e7-4d5a-8c92-25a8c8e855f1)

-- Bài relu
![Screenshot 2024-10-21 181550](https://github.com/user-attachments/assets/a87c24b7-bc8f-402f-bd3b-e817fcfe9bbd)

