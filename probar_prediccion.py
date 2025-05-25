import cv2
import os
from Lsa64_Model import predict_sign

# Cambia esta ruta a la carpeta del video que quieres probar
carpeta = "dataset_frames/B/001"  # ejemplo: letra B, video 001

frames = []
for i in range(20):
    ruta = os.path.join(carpeta, f"{i:03}.jpg")
    if not os.path.exists(ruta):
        print(f"⛔ Frame faltante: {ruta}")
        break
    img = cv2.imread(ruta)
    frames.append(img)

if len(frames) == 20:
    letra = predict_sign(frames)
    print(f"✅ Letra detectada: {letra}")
else:
    print("❌ No se pudo predecir. Faltan frames.")
