import os
import cv2
import numpy as np
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import TimeDistributed, Conv2D, MaxPooling2D, Flatten, LSTM, Dense

# Configuración reducida
FRAMES_DIR = "dataset_frames"
FRAMES_POR_VIDEO = 20
FRAME_SIZE = (64, 64)
CLASES = list("ABCDEFGHIJ")  # solo 10 letras

# Cargar los datos
X = []
y = []

print("📦 Cargando datos reducidos...")

for idx, letra in enumerate(CLASES):
    letra_dir = os.path.join(FRAMES_DIR, letra)
    if not os.path.exists(letra_dir):
        continue
    videos = os.listdir(letra_dir)[:20]  # solo 20 videos por letra
    for video in videos:
        video_path = os.path.join(letra_dir, video)
        frames = []
        for i in range(FRAMES_POR_VIDEO):
            frame_path = os.path.join(video_path, f"{i:03}.jpg")
            if os.path.exists(frame_path):
                img = cv2.imread(frame_path)
                img = cv2.resize(img, FRAME_SIZE)
                frames.append(img)
        if len(frames) == FRAMES_POR_VIDEO:
            X.append(frames)
            y.append(idx)

X = np.array(X, dtype=np.float32) / 255.0
y = to_categorical(y, num_classes=len(CLASES))

print(f"✅ Datos cargados: {X.shape}, Labels: {y.shape}")

# División entrenamiento/validación
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear modelo simple LSTM-CNN
print("🛠️ Construyendo el modelo...")
model = Sequential([
    TimeDistributed(Conv2D(16, (3, 3), activation='relu'), input_shape=(FRAMES_POR_VIDEO, *FRAME_SIZE, 3)),
    TimeDistributed(MaxPooling2D(2, 2)),
    TimeDistributed(Flatten()),
    LSTM(64),
    Dense(128, activation='relu'),
    Dense(len(CLASES), activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Entrenamiento
print("🚀 Entrenando el modelo...")
history = model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=10, batch_size=16)

# Guardar modelo
model.save("sign_language_model_reducido.h5")
print("📁 Modelo guardado como sign_language_model_reducido.h5")