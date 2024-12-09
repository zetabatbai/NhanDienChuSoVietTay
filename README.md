# Xây dựng hệ thống nhận diện chữ số viết tay
## Giới Thiệu
###### Dự án này được phát triển như một phần của môn học Xử Lý Ảnh và Thị Giác Máy Tính. Hệ thống tập trung vào việc nhận diện chữ số viết tay  sử dụng mô hình Linear SVC (Linear Support Vector Machine)
###### Dự án được thực hiện bởi nhóm sinh viên Nhóm 9 - CNTT12.10.2 trường Đại học Công Nghệ Đông Á
###### •	Môn học: Xử Lý Ảnh và Thị Giác Máy Tính
###### •	Giảng viên hướng dẫn: LƯƠNG THỊ HỒNG LAN
###### •	Ngày báo cáo: 07/12/2024
## Thành Viên Nhóm
###### Phan Thị Phương Thảo
###### Bùi Thị Thư
###### Trần Thúy Hiền
###### Lê Thị Minh
## Tính Năng Chính
### Huấn luyện số nhận dạng mô hình:
###### •	Huấn luyện SVM mô hình bằng cách sử dụng HOG cụ thể trên MNIST dữ liệu.
###### •	Lưu mô hình huấn luyện để tái sử dụng.
### Số nhận dạng ứng dụng trên hình ảnh (GUI):
###### •	Choose image: Cho phép người dùng tải ảnh lên từ máy tính.
###### •	Xử lý nhận dạng: Phát hiện các số trong hình ảnh, dự kiến các số và hiển thị kết quả lên hình ảnh.
###### •	Hiển thị ảnh: Hiển thị ảnh gốc và ảnh đã được xử lý trong giao diện.
### Cảnh báo người dùng:
###### •	Hiển thị thông báo nếu chưa chọn ảnh mà nhấn nút nhận dạng.
## Công Nghệ Sử Dụng
### •	Ngôn ngữ: Python
### •	Thư viện chính:
###### OpenCV
###### NumPy
###### scikit-image
###### scikit-learn
###### TensorFlow
###### scikit-learn
###### joblib
###### os
###### tkinter
###### Pillow
### •	Mô hình: LinearSVC
## Kết Quả Đạt Được
###### •	 Hệ thống có thể nhận diện các chữ số viết tay với độ chính xác cao trên tập MNIST.
###### •	 Giao diện thân thiện với người dùng, cho phép tải ảnh và xem kết quả trực tiếp.
# SLIDE Báo cáo:
###### https://www.canva.com/design/DAGYgO1IhXE/x17chTQn8EQLakNlweS9_g/edit?utm_content=DAGYgO1IhXE&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
# WORD BÁO CÁO:
###### https://drive.google.com/file/d/1gpS3JrtwGFLwy9VeVkK88NUbb0BmACKY/view?usp=sharing

#
