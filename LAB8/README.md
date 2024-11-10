# Ma Trận Nhầm Lẫn
Ma trận nhầm lẫn là một bảng được sử dụng để đánh giá hiệu suất của mô hình phân loại. Nó so sánh các nhãn thật của dữ liệu với các nhãn dự đoán của mô hình. Ma trận giúp ta hiểu rõ những loại lỗi mà mô hình gặp phải và những lớp (class) nào dễ bị phân loại sai.
## Cấu Trúc của Ma Trận Nhầm Lẫn
Ma trận nhầm lẫn thường có dạng sau đối với bài toán phân loại nhị phân:

![image](https://github.com/user-attachments/assets/24f5f146-f9d5-4980-b039-f845735f9830)
### Ma trận nhầm lẫn cũng có thể trực quan hóa kết quả cho các bài toán phân loại đa lớp

![image](https://github.com/user-attachments/assets/6820c999-3284-4a14-a0f6-b588d42c29ff)

## Tại Sao Ma Trận Nhầm Lẫn Quan Trọng?
Giúp nhận diện các lỗi phân loại: Ma trận cho phép ta biết được mô hình hay phân loại sai ở những lớp nào.
Cải thiện hiệu suất mô hình: Phân tích ma trận nhầm lẫn giúp ta nhận diện được những điểm yếu trong mô hình và cải thiện nó, chẳng hạn như điều chỉnh các tham số của mô hình, thu thập thêm dữ liệu hoặc sử dụng thuật toán khác.
Cải thiện việc hiểu các chỉ số: Khi nhìn vào ma trận nhầm lẫn, ta có thể tính toán các chỉ số hiệu suất như độ chính xác, recall, precision, F1-score một cách dễ dàng hơn.

### Ma trận nhầm lẫn cho dữ liệu nhị phân

### Ma trận nhần lẫn và các chỉ số cho Wine dataset
![Screenshot 2024-11-11 040047](https://github.com/user-attachments/assets/3459d831-e2f0-4909-b6f5-f9d03de438a7)
