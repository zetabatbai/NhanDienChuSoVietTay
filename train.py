import cv2
import numpy as np
from skimage.feature import hog
from sklearn.svm import LinearSVC
import tensorflow as tf
from sklearn.metrics import accuracy_score, f1_score
import joblib  # Lưu và tải mô hình
import os

# Tắt các cảnh báo liên quan đến TensorFlow
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# Load dữ liệu MNIST
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

# Tiền xử lý dữ liệu: chuẩn hóa ảnh (từ 0-255 thành 0-1)
X_train = X_train.astype(np.float32) / 255.0
X_test = X_test.astype(np.float32) / 255.0

# Trích xuất đặc trưng HOG cho X_train
X_train_feature = []
for i in range(len(X_train)):
    feature = hog(X_train[i], orientations=9, pixels_per_cell=(14, 14),
                  cells_per_block=(1, 1), block_norm="L2-Hys", visualize=False)
    X_train_feature.append(feature)
X_train_feature = np.array(X_train_feature, dtype=np.float32)

# Trích xuất đặc trưng HOG cho X_test
X_test_feature = []
for i in range(len(X_test)):
    feature = hog(X_test[i], orientations=9, pixels_per_cell=(14, 14),
                  cells_per_block=(1, 1), block_norm="L2-Hys", visualize=False)
    X_test_feature.append(feature)
X_test_feature = np.array(X_test_feature, dtype=np.float32)

# Huấn luyện mô hình LinearSVC
model = LinearSVC(C=10)
model.fit(X_train_feature, y_train)

# Dự đoán trên tập test
y_pred = model.predict(X_test_feature)

# Tính toán độ chính xác (Accuracy) và F1-score
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average='weighted')  # Sử dụng 'weighted' để tính trung bình có trọng số theo số mẫu từng lớp

print(f"Độ chính xác (Accuracy): {accuracy:.2f}")
print(f"F1-score (Weighted): {f1:.2f}")

# Lưu mô hình vào file
joblib.dump(model, 'linear_svc_model.pkl')
print("Model đã được lưu vào file 'linear_svc_model.pkl'")
