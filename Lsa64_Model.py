import os
import cv2
import numpy as np
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import TimeDistributed, Conv2D, MaxPooling2D, Flatten, LSTM, Dense, Dropout

# Configuración reducida para prueba
FRAMES_DIR = "dataset_frames"
FRAMES_POR_VIDEO = 20
FRAME_SIZE = (64, 64)
CLASES = list("ABCDEFGHIJ")

X = []
y = []

print("📦 Cargando datos reducidos de prueba...")

for idx, letra in enumerate(CLASES):
    letra_dir = os.path.join(FRAMES_DIR, letra)
    if not os.path.exists(letra_dir):
        print(f"⚠️ Carpeta no encontrada: {letra_dir}")
        continue
    videos = os.listdir(letra_dir)  # usa todos los disponibles
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
#        else:
#            print(f"⛔ Video incompleto: {video_path} — {len(frames)} frames encontrados")

X = np.array(X, dtype=np.float32) / 255.0
y = to_categorical(y, num_classes=len(CLASES))

print(f"✅ Datos cargados: {X.shape}, Labels: {y.shape}")

if len(X) < 2:
    print("❌ No hay suficientes datos para entrenar. Se necesitan al menos 2 muestras.")
    exit()

# División entrenamiento/validación
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear modelo LSTM-CNN con Dropout
print("🛠️ Construyendo el modelo...")
model = Sequential([
    TimeDistributed(Conv2D(16, (3, 3), activation='relu'), input_shape=(FRAMES_POR_VIDEO, *FRAME_SIZE, 3)),
    TimeDistributed(MaxPooling2D(2, 2)),
    TimeDistributed(Flatten()),
    LSTM(64),
    Dropout(0.4),
    Dense(128, activation='relu'),
    Dropout(0.3),
    Dense(len(CLASES), activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Entrenamiento (ligero)
print("🚀 Entrenando el modelo...")
model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=5, batch_size=4)

# Guardar modelo
model.save("app/modelos/sign_language_model_reducido.h5")
print("📁 Modelo guardado como sign_language_model_reducido.h5 ✅")

def predict_sign(frames):
    if len(frames) != FRAMES_POR_VIDEO:
        raise ValueError("Se requieren exactamente 20 frames para la predicción")
    frames_resized = [cv2.resize(f, FRAME_SIZE) for f in frames]
    frames_np = np.array(frames_resized, dtype=np.float32) / 255.0
    input_modelo = np.expand_dims(frames_np, axis=0)
    pred = model.predict(input_modelo)
    idx = np.argmax(pred)
    letra = CLASES[idx]
    return letra
