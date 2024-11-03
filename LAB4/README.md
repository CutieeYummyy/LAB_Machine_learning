# LAB 4 : Desicion Tree và Random Forest 
## Decision Tree 
Cây quyết định (DT) là một phương pháp học có giám sát phi tham số được sử dụng để phân loại và hồi quy . Mục tiêu là tạo ra một mô hình dự đoán giá trị của một biến mục tiêu bằng cách học các quy tắc quyết định đơn giản được suy ra từ các tính năng dữ liệu. Một cây có thể được coi là một phép xấp xỉ hằng số từng phần. Decision Tree là thuật toán supervised learning, có thể giải quyết cả bài toán regression và classification.
### Một số ưu điểm của cây quyết định là:
- Dễ hiểu và dễ diễn giải. Có thể trực quan hóa cây cối.
- Yêu cầu ít chuẩn bị dữ liệu. Các kỹ thuật khác thường yêu cầu chuẩn hóa dữ liệu, cần tạo các biến giả và xóa các giá trị trống. Một số kết hợp cây và thuật toán hỗ trợ các giá trị bị thiếu .
- Chi phí sử dụng cây (tức là dự đoán dữ liệu) là logarit theo số điểm dữ liệu được sử dụng để đào tạo cây.
- Có thể xử lý cả dữ liệu số và dữ liệu phân loại. Tuy nhiên, hiện tại, triển khai scikit-learn không hỗ trợ các biến phân loại. Các kỹ thuật khác thường chuyên phân tích các tập dữ liệu chỉ có một loại biến. Xem thuật toán để biết thêm thông tin.
- Có khả năng xử lý các vấn đề liên quan đến nhiều đầu ra.
- Sử dụng mô hình hộp trắng. Nếu một tình huống nhất định có thể quan sát được trong mô hình, lời giải thích cho tình huống đó có thể dễ dàng được giải thích bằng logic boolean. Ngược lại, trong mô hình hộp đen (ví dụ, trong mạng nơ-ron nhân tạo), kết quả có thể khó diễn giải hơn.
- Có thể xác thực mô hình bằng các thử nghiệm thống kê. Điều đó giúp tính đến độ tin cậy của mô hình.
- Hoạt động tốt ngay cả khi các giả định của nó bị vi phạm phần nào bởi mô hình thực tế mà dữ liệu được tạo ra.
### Những nhược điểm của cây quyết định bao gồm:
- Có thể tạo ra các cây quá phức tạp không khái quát hóa dữ liệu tốt. Điều này được gọi là quá khớp. Các cơ chế như cắt tỉa, thiết lập số lượng mẫu tối thiểu cần thiết tại một nút lá hoặc thiết lập độ sâu tối đa của cây là cần thiết để tránh vấn đề này.
- Cây quyết định có thể không ổn định vì những thay đổi nhỏ trong dữ liệu có thể dẫn đến việc tạo ra một cây hoàn toàn khác. Vấn đề này được giảm nhẹ bằng cách sử dụng cây quyết định trong một tập hợp.
Dự đoán của cây quyết định không phải là trơn tru hay liên tục, mà là các phép xấp xỉ hằng số từng phần như trong hình trên. Do đó, chúng không tốt cho việc ngoại suy.
- Có những khái niệm khó học vì cây quyết định không thể hiện chúng một cách dễ dàng, chẳng hạn như các bài toán XOR, chẵn lẻ hoặc ghép kênh.
- Cây quyết định tạo ra các cây thiên vị nếu một số lớp chiếm ưu thế. Do đó, nên cân bằng tập dữ liệu trước khi phù hợp với cây quyết định.
### DecisionTreeClassifier 
DecisionTreeClassifier là một lớp có khả năng thực hiện phân loại đa lớp trên một tập dữ liệu.
Giống như các bộ phân loại khác, DecisionTreeClassifierlấy đầu vào là hai mảng: một mảng X, thưa thớt hoặc dày đặc, có hình dạng chứa các mẫu đào tạo và một mảng Y có giá trị nguyên, có hình dạng , chứa nhãn lớp cho các mẫu đào tạo:(n_samples, n_features)(n_samples,)
Cây quyết định bắt đầu bằng một nút gốc, không có bất kỳ nhánh nào đến. Các nhánh đi ra từ nút gốc sau đó đưa vào các nút bên trong, còn được gọi là các nút quyết định. Dựa trên các tính năng có sẵn, cả hai loại nút đều tiến hành đánh giá để tạo thành các tập hợp con đồng nhất, được biểu thị bằng các nút lá hoặc nút đầu cuối. Các nút lá biểu thị tất cả các kết quả có thể có trong tập dữ liệu.
![image](https://github.com/user-attachments/assets/0113bc4c-b4ac-4f73-94da-0f51fd7d2e4e)
### Ví dụ về tập dữ liệu khác
![Screenshot 2024-11-03 205627](https://github.com/user-attachments/assets/2b6779b2-902a-44de-a5b7-e54db0780435)
![Screenshot 2024-11-03 205646](https://github.com/user-attachments/assets/ec834538-7c5d-4ee9-8494-c30897844caa)

## Random Forest
Random Forest là một thuật toán học máy thường được sử dụng, được đăng ký nhãn hiệu bởi Leo Breiman và Adele Cutler, kết hợp đầu ra của nhiều cây quyết định để đạt được một kết quả duy nhất. Tính dễ sử dụng và tính linh hoạt của nó đã thúc đẩy việc áp dụng, vì nó xử lý cả các vấn đề phân loại và hồi quy.
Random là ngẫu nhiên, Forest là rừng, nên ở thuật toán Random Forest mình sẽ xây dựng nhiều cây quyết định bằng thuật toán Decision Tree, tuy nhiên mỗi cây quyết định sẽ khác nhau (có yếu tố random). Sau đó kết quả dự đoán được tổng hợp từ các cây quyết định.
Ở bước huấn luyện thì mình sẽ xây dựng nhiều cây quyết định, các cây quyết định có thể khác nhau (phần sau mình sẽ nói mỗi cây được xây dựng như thế nào).
![image](https://github.com/user-attachments/assets/e4d3445e-ad60-4dc8-9f55-b7a37ea6154e)
Sau đó ở bước dự đoán, với một dữ liệu mới, thì ở mỗi cây quyết định mình sẽ đi từ trên xuống theo các node điều kiện để được các dự đoán, sau đó kết quả cuối cùng được tổng hợp từ kết quả của các cây quyết định.
![image](https://github.com/user-attachments/assets/91ee3111-7c52-42a3-a38c-8e942bf2115a)
Ví dụ như trên, thuật toán Random Forest có 6 cây quyết định, 5 cây dự đoán 1 và 1 cây dự đoán 0, do đó mình sẽ vote là cho ra dự đoán cuối cùng là 1.
Xây dựng thuật toán Random Forest.
- Giả sử bộ dữ liệu của mình có n dữ liệu (sample) và mỗi dữ liệu có d thuộc tính (feature).
Để xây dựng mỗi cây quyết định mình sẽ làm như sau:
-- Lấy ngẫu nhiên n dữ liệu từ bộ dữ liệu với kĩ thuật Bootstrapping, hay còn gọi là random sampling with replacement. Tức khi mình sample được 1 dữ liệu thì mình không bỏ dữ liệu đấy ra mà vẫn giữ lại trong tập dữ liệu ban đầu, rồi tiếp tục sample cho tới khi sample đủ n dữ liệu. Khi dùng kĩ thuật này thì tập n dữ liệu mới của mình có thể có những dữ liệu bị trùng nhau.
-- Sau khi sample được n dữ liệu từ bước 1 thì mình chọn ngẫu nhiên ở k thuộc tính (k < n). Giờ mình được bộ dữ liệu mới gồm n dữ liệu và mỗi dữ liệu có k thuộc tính.
-- Dùng thuật toán Decision Tree để xây dựng cây quyết định với bộ dữ liệu ở bước 2.
### Dù có độ chính xác khá cao nhưng cây quyết định tồn tại những hạn chế lớn đó là:
- Dễ xảy ra quá khớp nếu số lượng các đặc trưng để hỏi lớn. Khi độ sâu của cây quyết định không bị giới hạn thì có thể tạo ra những node lá chỉ có một vài quan sát. Những kết luận dự báo từ chúng thường chỉ đúng trên tập huấn luyện mà không đúng trên tập kiểm tra.
- Trong tình huống bộ dữ liệu có số lượng biến lớn. Một cây quyết định có độ sâu giới hạn (để giảm thiểu quá khớp) thường bỏ sót những biến quan trọng.
- Cây quyết định chỉ tạo ra một kịch bản dự báo duy nhất cho mỗi một quan sát nên nếu model có hiệu suất kém thì kết quả sẽ bị chệch.
### Ví dụ về bộ dữ liệu khác
![image](https://github.com/user-attachments/assets/7798d17e-c2ed-4439-b4ab-1c8513421c23)
![Uploading image.png…]()

