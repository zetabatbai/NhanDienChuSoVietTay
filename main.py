import tkinter as tk
from tkinter import filedialog, messagebox  # Thêm import messagebox

import cv2
import joblib
import numpy as np
from PIL import Image, ImageTk
from skimage.feature import hog

# Sửa lỗi tên file mô hình
model = joblib.load('linear_svc_model.pkl')


def load_image():
    """Hàm để chọn và hiển thị ảnh gốc trong frame bên trái."""
    global original_image, processed_image

    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
    if file_path:
        # Tải và hiển thị ảnh gốc
        original_image = cv2.imread(file_path)
        original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)  # Chuyển sang RGB
        display_image(original_image, left_frame)

        # Đặt processed_image về None mỗi khi tải ảnh mới
        processed_image = None
        clear_frame(right_frame)


def recognize_image():
    """Hàm để xử lý nhận diện ảnh và hiển thị kết quả trong frame bên phải."""
    global original_image, processed_image

    if original_image is not None:
        # Giả lập xử lý nhận diện (ở đây chỉ chuyển ảnh sang mức xám)
        im_gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
        im_blur = cv2.GaussianBlur(im_gray, (5, 5), 0)
        _, thre = cv2.threshold(im_blur, 90, 255, cv2.THRESH_BINARY_INV)
        contours, hierachy = cv2.findContours(thre, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # Sửa lỗi unpack

        rects = [cv2.boundingRect(cnt) for cnt in contours]

        for i in contours:
            (x, y, w, h) = cv2.boundingRect(i)
            cv2.rectangle(original_image, (x, y), (x + w, y + h), (0, 255, 0), 3)
            roi = thre[y:y + h, x:x + w]
            roi = np.pad(roi, (20, 20), 'constant', constant_values=(0, 0))
            roi = cv2.resize(roi, (28, 28), interpolation=cv2.INTER_AREA)
            roi = cv2.dilate(roi, (3, 3))

            # Tính toán các đặc trưng HOG
            roi_hog_fd = hog(roi, orientations=9, pixels_per_cell=(14, 14), cells_per_block=(1, 1), block_norm="L2")
            nbr = model.predict(np.array([roi_hog_fd], np.float32))

            # Đặt vị trí văn bản bên trái hộp giới hạn
            offset = 10  # Khoảng cách từ cạnh trái của hộp giới hạn
            text_x = x - offset  # Vị trí văn bản bên trái hộp giới hạn
            text_y = y + h // 2  # Căn chỉnh văn bản theo chiều dọc trong hộp giới hạn
            processed_image = cv2.putText(original_image, str(int(nbr[0])), (text_x, text_y), cv2.FONT_HERSHEY_DUPLEX, 2,
                                          (0, 255, 255), 3)

        # Hiển thị ảnh sau khi xử lý
        display_image(processed_image, right_frame)

    else:
        messagebox.showwarning("Cảnh báo", "Hãy tải ảnh trước khi nhận diện!")  # Hiển thị cảnh báo nếu chưa tải ảnh


def display_image(image, frame):
    """Hàm hiển thị ảnh trong một frame."""
    clear_frame(frame)  # Xóa nội dung trong frame trước khi hiển thị ảnh

    # Resize ảnh để phù hợp với frame
    height, width = image.shape[:2]
    max_width, max_height = 500, 500  # Kích thước tối đa để hiển thị (cập nhật kích thước lớn hơn)
    scale = min(max_width / width, max_height / height)
    resized_image = cv2.resize(image, (int(width * scale), int(height * scale)))

    # Chuyển ảnh sang định dạng hiển thị với Tkinter
    im = Image.fromarray(resized_image)
    im_tk = ImageTk.PhotoImage(image=im)

    # Tạo nhãn chứa ảnh và hiển thị
    label = tk.Label(frame, image=im_tk)
    label.image = im_tk  # Giữ tham chiếu để tránh bị xóa bộ nhớ
    label.pack()


def clear_frame(frame):
    """Hàm xóa toàn bộ nội dung trong frame."""
    for widget in frame.winfo_children():
        widget.destroy()


# Tạo cửa sổ chính
root = tk.Tk()
root.title("Nhận diện ảnh với Tkinter")

# Khởi tạo các biến toàn cục
original_image = None
processed_image = None

# Tạo các frame
left_frame = tk.Frame(root, width=500, height=500, bg="lightgray")  # Kích thước lớn hơn
left_frame.pack(side="left", padx=10, pady=10)
left_frame.pack_propagate(False)

right_frame = tk.Frame(root, width=500, height=500, bg="lightgray")  # Kích thước lớn hơn
right_frame.pack(side="right", padx=10, pady=10)
right_frame.pack_propagate(False)

# Tạo nút chọn ảnh và nhận diện ảnh
button_frame = tk.Frame(root)
button_frame.pack(side="top", pady=10)

load_button = tk.Button(button_frame, text="Chọn ảnh", command=load_image)
load_button.pack(side="left", padx=10)

recognize_button = tk.Button(button_frame, text="Nhận diện", command=recognize_image)
recognize_button.pack(side="right", padx=10)

# Chạy vòng lặp chính
root.mainloop()
